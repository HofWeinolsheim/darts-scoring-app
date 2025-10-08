import psycopg2
import psycopg2.extras
import os
from datetime import datetime
import uuid

class DartsDatabase:
    def __init__(self):
        self.connection = None
        self.connect()
        self.create_tables()
    
    def connect(self):
        """Connect to Railway PostgreSQL database"""
        try:
            # Use DATABASE_URL from Railway if available, otherwise fallback to hardcoded internal URL
            database_url = os.getenv(
                "DATABASE_URL",
                "postgresql://postgres:xwoxXKKbBYKiKlJLhMJyWuccrWUmMDVa@postgres.railway.internal:5432/railway"
            )

            # psycopg2 requires postgresql:// prefix
            if database_url.startswith("postgres://"):
                database_url = database_url.replace("postgres://", "postgresql://", 1)

            self.connection = psycopg2.connect(database_url)
            self.connection.autocommit = True
            print("✅ Successfully connected to Railway PostgreSQL database")
                
        except Exception as e:
            print(f"❌ Error connecting to PostgreSQL: {e}")
            print("App will continue with limited functionality")
            self.connection = None
    
    def create_tables(self):
        """Create necessary tables if they don't exist"""
        if not self.connection:
            print("⚠️ No database connection - skipping table creation")
            return
        
        cursor = self.connection.cursor()
        
        players_table = """
        CREATE TABLE IF NOT EXISTS players (
            id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            pin_code VARCHAR(4),
            is_guest BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        games_table = """
        CREATE TABLE IF NOT EXISTS games (
            id VARCHAR(36) PRIMARY KEY,
            game_mode INTEGER NOT NULL,
            tournament_mode VARCHAR(20),
            tournament_id VARCHAR(36),
            winner_id VARCHAR(36),
            rounds INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        participants_table = """
        CREATE TABLE IF NOT EXISTS game_participants (
            id VARCHAR(36) PRIMARY KEY,
            game_id VARCHAR(36) NOT NULL,
            player_id VARCHAR(36) NOT NULL,
            final_score INTEGER NOT NULL,
            total_scored INTEGER NOT NULL,
            rounds_played INTEGER NOT NULL,
            average_score DECIMAL(5,2)
        )
        """
        
        indexes = [
            "CREATE INDEX IF NOT EXISTS idx_games_winner ON games(winner_id)",
            "CREATE INDEX IF NOT EXISTS idx_participants_game ON game_participants(game_id)",
            "CREATE INDEX IF NOT EXISTS idx_participants_player ON game_participants(player_id)"
        ]
        
        try:
            cursor.execute(players_table)
            cursor.execute(games_table)
            cursor.execute(participants_table)
            for index in indexes:
                cursor.execute(index)
            print("✅ Database tables created successfully")
        except Exception as e:
            print(f"❌ Error creating tables: {e}")
        finally:
            cursor.close()
    
    def save_player(self, player_data):
        """Save a player profile"""
        if not self.connection:
            return False
        
        cursor = self.connection.cursor()
        query = """
        INSERT INTO players (id, name, pin_code, is_guest) 
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET 
        name = EXCLUDED.name, pin_code = EXCLUDED.pin_code
        """
        
        try:
            cursor.execute(query, (
                player_data['id'],
                player_data['name'],
                player_data.get('pin_code'),
                player_data.get('is_guest', False)
            ))
            return True
        except Exception as e:
            print(f"❌ Error saving player: {e}")
            return False
        finally:
            cursor.close()
    
    def get_players(self):
        """Get all non-guest players"""
        if not self.connection:
            return []
        
        cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT * FROM players WHERE is_guest = FALSE ORDER BY name"
        
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"❌ Error fetching players: {e}")
            return []
        finally:
            cursor.close()
    
    def save_game(self, game_data):
        """Save a game record with participants"""
        if not self.connection:
            return False
        
        cursor = self.connection.cursor()
        
        try:
            game_query = """
            INSERT INTO games (id, game_mode, tournament_mode, winner_id, rounds)
            VALUES (%s, %s, %s, %s, %s)
            """
            
            game_id = str(uuid.uuid4())
            cursor.execute(game_query, (
                game_id,
                game_data['gameMode'],
                game_data.get('tournamentMode'),
                game_data['winner']['id'],
                game_data['rounds']
            ))
            
            participant_query = """
            INSERT INTO game_participants 
            (id, game_id, player_id, final_score, total_scored, rounds_played, average_score)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            
            for player in game_data['players']:
                if not player.get('profile', {}).get('isGuest', False):
                    total_scored = sum(player['rounds'])
                    average_score = total_scored / len(player['rounds']) if player['rounds'] else 0
                    
                    cursor.execute(participant_query, (
                        str(uuid.uuid4()),
                        game_id,
                        player['id'],
                        player['currentScore'],
                        total_scored,
                        len(player['rounds']),
                        average_score
                    ))
            
            return True
        except Exception as e:
            print(f"❌ Error saving game: {e}")
            return False
        finally:
            cursor.close()
    
    def get_player_stats(self, player_id):
        """Get comprehensive statistics for a player"""
        if not self.connection:
            return {}
        
        cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        try:
            stats_query = """
            SELECT 
                COUNT(*) as total_games,
                SUM(CASE WHEN g.winner_id = %s THEN 1 ELSE 0 END) as wins,
                AVG(gp.average_score) as overall_average,
                MAX(gp.total_scored) as best_game,
                SUM(gp.total_scored) as total_points
            FROM game_participants gp
            JOIN games g ON gp.game_id = g.id
            WHERE gp.player_id = %s
            """
            
            cursor.execute(stats_query, (player_id, player_id))
            stats = cursor.fetchone()
            
            recent_query = """
            SELECT g.game_mode, g.created_at, 
                   CASE WHEN g.winner_id = %s THEN 'Win' ELSE 'Loss' END as result,
                   gp.total_scored, gp.average_score
            FROM games g
            JOIN game_participants gp ON g.id = gp.game_id
            WHERE gp.player_id = %s
            ORDER BY g.created_at DESC
            LIMIT 5
            """
            
            cursor.execute(recent_query, (player_id, player_id))
            recent_games = cursor.fetchall()
            
            return {
                'stats': dict(stats) if stats else {},
                'recent_games': [dict(game) for game in recent_games]
            }
        except Exception as e:
            print(f"❌ Error fetching player stats: {e}")
            return {}
        finally:
            cursor.close()
    
    def get_leaderboard(self):
        """Get leaderboard data"""
        if not self.connection:
            return []
        
        cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        query = """
        SELECT 
            p.name,
            COUNT(*) as total_games,
            SUM(CASE WHEN g.winner_id = p.id THEN 1 ELSE 0 END) as wins,
            ROUND(SUM(CASE WHEN g.winner_id = p.id THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) as win_rate,
            ROUND(AVG(gp.average_score), 1) as avg_score
        FROM players p
        JOIN game_participants gp ON p.id = gp.player_id
        JOIN games g ON gp.game_id = g.id
        WHERE p.is_guest = FALSE
        GROUP BY p.id, p.name
        HAVING COUNT(*) > 0
        ORDER BY win_rate DESC, avg_score DESC
        """
        
        try:
            cursor.execute(query)
            return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            print(f"❌ Error fetching leaderboard: {e}")
            return []
        finally:
            cursor.close()
    
    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()

# Global database instance
db = DartsDatabase()

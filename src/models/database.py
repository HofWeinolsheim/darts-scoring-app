import pymysql
import os
from datetime import datetime
import uuid

class DartsDatabase:
    def __init__(self):
        self.connection = None
        self.connect()
        self.create_tables()
    
    def connect(self):
        """Connect to the MySQL database using environment variables"""
        try:
            self.connection = pymysql.connect(
                host=os.getenv('DB_HOST', 'db501876797.hosting-data.io'),
                port=int(os.getenv('DB_PORT', 3306)),
                database=os.getenv('DB_NAME', 'dbs14837239'),
                user=os.getenv('DB_USER', 'dbu738581'),
                password=os.getenv('DB_PASSWORD', 'darts@1661'),
                charset='utf8mb4',
                autocommit=True,
                connect_timeout=30
            )
            print("Successfully connected to MySQL database")
        except Exception as e:
            print(f"Error connecting to MySQL: {e}")
            print("App will continue with fallback mode")
            self.connection = None
    
    def create_tables(self):
        """Create necessary tables if they don't exist"""
        if not self.connection:
            print("No database connection - skipping table creation")
            return
        
        cursor = self.connection.cursor()
        
        # Players table
        players_table = """
        CREATE TABLE IF NOT EXISTS players (
            id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            pin_code VARCHAR(4),
            is_guest BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        # Games table
        games_table = """
        CREATE TABLE IF NOT EXISTS games (
            id VARCHAR(36) PRIMARY KEY,
            game_mode INT NOT NULL,
            tournament_mode VARCHAR(20),
            tournament_id VARCHAR(36),
            winner_id VARCHAR(36),
            rounds INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_winner (winner_id)
        )
        """
        
        # Game participants table
        participants_table = """
        CREATE TABLE IF NOT EXISTS game_participants (
            id VARCHAR(36) PRIMARY KEY,
            game_id VARCHAR(36) NOT NULL,
            player_id VARCHAR(36) NOT NULL,
            final_score INT NOT NULL,
            total_scored INT NOT NULL,
            rounds_played INT NOT NULL,
            average_score DECIMAL(5,2),
            INDEX idx_game (game_id),
            INDEX idx_player (player_id)
        )
        """
        
        try:
            cursor.execute(players_table)
            cursor.execute(games_table)
            cursor.execute(participants_table)
            print("Database tables created successfully")
        except Exception as e:
            print(f"Error creating tables: {e}")
            raise e
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
        ON DUPLICATE KEY UPDATE 
        name = VALUES(name), pin_code = VALUES(pin_code)
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
            print(f"Error saving player: {e}")
            return False
        finally:
            cursor.close()
    
    def get_players(self):
        """Get all non-guest players"""
        if not self.connection:
            return []
        
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        query = "SELECT * FROM players WHERE is_guest = FALSE ORDER BY name"
        
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching players: {e}")
            return []
        finally:
            cursor.close()
    
    def save_game(self, game_data):
        """Save a game record with participants"""
        if not self.connection:
            return False
        
        cursor = self.connection.cursor()
        
        try:
            # Insert game
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
            
            # Insert participants
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
            print(f"Error saving game: {e}")
            return False
        finally:
            cursor.close()
    
    def get_player_stats(self, player_id):
        """Get comprehensive statistics for a player"""
        if not self.connection:
            return {}
        
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        
        try:
            # Get basic stats
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
            
            # Get recent games
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
                'stats': stats,
                'recent_games': recent_games
            }
        except Exception as e:
            print(f"Error fetching player stats: {e}")
            return {}
        finally:
            cursor.close()
    
    def get_leaderboard(self):
        """Get leaderboard data"""
        if not self.connection:
            return []
        
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        
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
        HAVING total_games > 0
        ORDER BY win_rate DESC, avg_score DESC
        """
        
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching leaderboard: {e}")
            return []
        finally:
            cursor.close()
    
    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()

# Global database instance
db = DartsDatabase()

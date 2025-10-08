from flask import Blueprint, request, jsonify
from src.models.railway_database import db
import uuid

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/players', methods=['GET'])
def get_players():
    """Get all non-guest players"""
    try:
        players = db.get_players()
        return jsonify(players)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/players', methods=['POST'])
def create_player():
    """Create a new player"""
    try:
        data = request.get_json()
        
        # Generate ID if not provided
        if 'id' not in data:
            data['id'] = str(uuid.uuid4())
        
        success = db.save_player(data)
        
        if success:
            return jsonify({'success': True, 'id': data['id']})
        else:
            return jsonify({'error': 'Failed to save player'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/games', methods=['POST'])
def save_game():
    """Save a game record"""
    try:
        data = request.get_json()
        success = db.save_game(data)
        
        if success:
            return jsonify({'success': True})
        else:
            return jsonify({'error': 'Failed to save game'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/stats/<player_id>', methods=['GET'])
def get_player_stats(player_id):
    """Get player statistics"""
    try:
        stats = db.get_player_stats(player_id)
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """Get leaderboard data"""
    try:
        leaderboard = db.get_leaderboard()
        return jsonify(leaderboard)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'database': 'connected' if db.connection else 'disconnected'})

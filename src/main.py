import os
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from src.routes.api import api_bp
from src.models.railway_database import db

# Load environment variables
load_dotenv( )

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# Set secret key
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Register API routes
app.register_blueprint(api_bp)

@app.route('/')
def serve_index():
    """Serve the main application"""
    try:
        return send_from_directory(app.static_folder, 'index.html')
    except Exception as e:
        return f"Error serving index.html: {str(e)}", 500

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files"""
    try:
        return send_from_directory(app.static_folder, path)
    except Exception as e:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

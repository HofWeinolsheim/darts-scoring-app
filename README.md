# 🎯 Professional Darts Scoring App

A comprehensive, mobile-friendly darts scoring application with tournament support, player profiles, and real-time statistics. Built with Flask backend and vanilla JavaScript frontend.

![Darts App Screenshot](https://via.placeholder.com/800x400/2c5530/ffffff?text=Darts+Scoring+App)

## ✨ Features

### 🎮 Game Modes
- **501 & 301 Games** - Classic darts countdown games
- **Tournament Modes** - Single Game, Best of 3, Best of 5
- **Multiplayer Support** - 2-6 players per game
- **Real-time Scoring** - Live score tracking and turn management

### 👤 Player Management
- **PIN-Protected Profiles** - Secure 4-digit PIN protection
- **Guest Mode** - Anonymous play without saving statistics
- **Player Selection** - Elegant modal-based player selection
- **Profile Persistence** - Automatic profile creation and reuse

### 📊 Advanced Statistics
- **Comprehensive Stats** - Games played, win rate, average scores
- **Tournament Tracking** - Separate tournament win records
- **Leaderboards** - Ranked player comparisons
- **Game History** - Detailed record of recent games
- **Real-time Averages** - Live calculation during games

### 🎨 Modern Design
- **Farmhouse Loft Theme** - Warm, professional color palette
- **Mobile-Optimized** - Touch-friendly interface for phones/tablets
- **Responsive Design** - Works perfectly on all screen sizes
- **Smooth Animations** - Professional UI transitions

### 🎉 Fun Features
- **Celebration Overlays** - Phil Taylor for 180s, laughing cat for misses
- **Quick Score Buttons** - Common dart scores for rapid entry
- **Undo Functionality** - Reverse last score entry
- **Miss Button** - Quick way to record 0 points

## 🗄️ Database Integration

- **MySQL 8.0 Support** - Full integration with IONOS MySQL
- **Automatic Schema** - Tables created automatically on first run
- **Environment Variables** - Secure credential management
- **Connection Fallback** - Graceful handling of connection issues

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- MySQL 8.0 database
- IONOS hosting account (or any server with MySQL access)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/darts-scoring-app.git
   cd darts-scoring-app
   ```

2. **Run the setup script**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

4. **Start the application**
   ```bash
   source venv/bin/activate
   python src/main.py
   ```

5. **Access your app**
   Open http://localhost:5000 in your browser

## 🔧 IONOS Deployment

### Step 1: Connect to Your Server
```bash
ssh your-username@your-server-ip
```

### Step 2: Clone and Setup
```bash
git clone https://github.com/your-username/darts-scoring-app.git
cd darts-scoring-app
./setup.sh
```

### Step 3: Start the App
```bash
source venv/bin/activate
python src/main.py
```

### Production Deployment
```bash
pip install gunicorn
gunicorn --bind 0.0.0.0:5000 --chdir src main:app
```

## 📁 Project Structure

```
darts_backend/
├── src/
│   ├── models/
│   │   └── database.py          # MySQL database integration
│   ├── routes/
│   │   └── api.py              # Flask API endpoints
│   ├── static/                 # Frontend files
│   │   ├── index.html
│   │   ├── assets/
│   │   └── components/
│   └── main.py                 # Flask application entry point
├── .env.example                # Environment variables template
├── requirements.txt            # Python dependencies
├── setup.sh                   # Automated setup script
├── DEPLOYMENT.md              # Detailed deployment guide
└── README.md                  # This file
```

## 🔌 API Endpoints

- `GET /api/players` - Get all players
- `POST /api/players` - Create new player
- `POST /api/games` - Save game record
- `GET /api/stats/{player_id}` - Get player statistics
- `GET /api/leaderboard` - Get leaderboard data
- `GET /api/health` - Database connection status

## 🎯 Game Rules

### Standard Play
- Players start with 501 or 301 points
- Score points to reduce total to exactly 0
- Turn rotates after each throw
- Game ends when a player reaches 0

### Tournament Mode
- **Best of 3**: First to win 2 games
- **Best of 5**: First to win 3 games
- Series score tracked throughout tournament

## 🔒 Security Features

- **PIN Protection** - 4-digit codes protect player profiles
- **Environment Variables** - Database credentials stored securely
- **Input Validation** - All scores validated (0-180 range)
- **SQL Injection Protection** - Parameterized queries

## 🛠️ Technical Details

### Backend
- **Flask** - Python web framework
- **PyMySQL** - MySQL database connector
- **Flask-CORS** - Cross-origin resource sharing
- **python-dotenv** - Environment variable management

### Frontend
- **Vanilla JavaScript** - No framework dependencies
- **CSS Grid/Flexbox** - Modern responsive layout
- **Local Storage Fallback** - Works offline if database unavailable
- **Progressive Web App** - Can be installed on mobile devices

### Database Schema
- **players** - Player profiles and PIN codes
- **games** - Game records and tournament data
- **game_participants** - Player statistics per game

## 🎨 Customization

### Theme Colors
The farmhouse loft theme uses:
- **Primary**: `#2c5530` (Forest Green)
- **Secondary**: `#f5f5dc` (Cream)
- **Accent**: `#8fbc8f` (Sage Green)
- **Text**: `#2c2c2c` (Charcoal)

### Adding New Celebrations
Add new celebration images to `src/static/assets/` and update the celebration logic in the main app component.

## 📱 Mobile Features

- **Touch-Friendly Buttons** - Large, easy-to-tap interface
- **Swipe Gestures** - Natural mobile interactions
- **Responsive Design** - Adapts to all screen sizes
- **Offline Capability** - Works without internet connection

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues:

1. Check the [DEPLOYMENT.md](DEPLOYMENT.md) guide
2. Verify your database connection with `/api/health`
3. Check the console logs for error messages
4. Ensure all environment variables are set correctly

## 🎯 Roadmap

- [ ] Multiple language support
- [ ] Advanced tournament brackets
- [ ] Player avatars and profiles
- [ ] Game replay functionality
- [ ] Export statistics to PDF
- [ ] Integration with dart board cameras

---

**Made with ❤️ for dart players everywhere**

*Enjoy your professional darts scoring experience!* 🎯

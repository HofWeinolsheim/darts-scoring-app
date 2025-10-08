# Darts Scorer App - IONOS Deployment Guide

## 📋 Prerequisites
- IONOS hosting account with SSH access
- Python 3.8+ installed on your server
- Your MySQL database credentials (already configured)

## 🚀 Deployment Steps

### 1. Upload Files to Your IONOS Server
```bash
# Upload the entire darts_backend folder to your server
scp -r darts_backend/ user@your-server:/path/to/your/app/
```

### 2. Server Setup
```bash
# SSH into your IONOS server
ssh user@your-server

# Navigate to app directory
cd /path/to/your/app/darts_backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit environment variables (already configured with your credentials)
nano .env
```

Your `.env` file contains:
```
DB_HOST=db501876797.hosting-data.io
DB_PORT=3306
DB_NAME=dbs14837239
DB_USER=dbu738581
DB_PASSWORD=darts@1661
FLASK_ENV=production
SECRET_KEY=darts_scorer_secret_key_2024
```

### 4. Test the Application
```bash
# Test locally first
python src/main.py

# Should show:
# Successfully connected to MySQL database
# Database tables created successfully
# * Running on all addresses (0.0.0.0)
# * Running on http://127.0.0.1:5000
```

### 5. Production Deployment with Gunicorn
```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn --bind 0.0.0.0:5000 --chdir src main:app
```

### 6. Process Management with PM2 (Recommended)
```bash
# Install PM2
npm install -g pm2

# Create PM2 ecosystem file
cat > ecosystem.config.js << EOF
module.exports = {
  apps: [{
    name: 'darts-scorer',
    script: 'gunicorn',
    args: '--bind 0.0.0.0:5000 --chdir src main:app',
    cwd: '/path/to/your/app/darts_backend',
    interpreter: '/path/to/your/app/darts_backend/venv/bin/python',
    env: {
      FLASK_ENV: 'production'
    }
  }]
};
EOF

# Start with PM2
pm2 start ecosystem.config.js
pm2 startup
pm2 save
```

### 7. Nginx Configuration (Optional)
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }
}
```

## 🗄️ Database Features

### Automatic Table Creation
The app automatically creates these tables in your MySQL database:
- `players` - Player profiles with PIN protection
- `games` - Game records with tournament support
- `game_participants` - Player statistics per game

### API Endpoints
- `GET /api/players` - Get all players
- `POST /api/players` - Create new player
- `POST /api/games` - Save game record
- `GET /api/stats/{player_id}` - Get player statistics
- `GET /api/leaderboard` - Get leaderboard data
- `GET /api/health` - Health check

## 🔧 Troubleshooting

### Database Connection Issues
```bash
# Test database connection
mysql -h db501876797.hosting-data.io -P 3306 -u dbu738581 -p dbs14837239
```

### Check Logs
```bash
# PM2 logs
pm2 logs darts-scorer

# Direct Flask logs
python src/main.py
```

### Firewall Settings
Ensure port 5000 (or your chosen port) is open:
```bash
sudo ufw allow 5000
```

## 🎯 Features Included

✅ **Modern Farmhouse Loft Theme**
✅ **PIN-Protected Player Profiles**
✅ **Guest Mode for Anonymous Play**
✅ **Tournament Modes** (Single, Best of 3, Best of 5)
✅ **Real-time Statistics and Leaderboards**
✅ **Celebration Overlays** (Phil Taylor for 180, Cat for misses)
✅ **Mobile-Optimized Interface**
✅ **Persistent MySQL Database Storage**

Your darts scoring app is now ready for production use on your IONOS server!

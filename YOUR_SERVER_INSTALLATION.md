# 🍎 Your IONOS Server - Mac Installation Guide

**Complete step-by-step guide using YOUR specific IONOS server details**

## 🎯 Your Server Information

**✅ I have your exact server details:**
- **Server:** access946050282.webspace-data.io
- **Port:** 22 (SSH)
- **Username:** acc429003293
- **Protocol:** SFTP/SSH

## 📍 Step 1: Download Your Darts App

1. **Download** the `darts-scoring-app.zip` file I provided
2. **Double-click** to extract it to your Desktop
3. **You should see a `darts_backend` folder**

---

## 💻 Step 2: Open Terminal on Your Mac

1. **Press `Cmd + Space`** (opens Spotlight)
2. **Type "Terminal"** and press Enter
3. **You'll see a black window** - this is your command line!

---

## 📤 Step 3: Upload Your App to IONOS Server

**Copy and paste this exact command in Terminal:**

```bash
# Go to your extracted app folder
cd ~/Desktop/darts_backend

# Upload everything to your IONOS server
scp -r . acc429003293@access946050282.webspace-data.io:~/darts-app/
```

**What happens:**
- You'll be asked for your IONOS password
- Type your password (you won't see characters - that's normal!)
- Files will upload to your server

---

## 🔐 Step 4: Connect to Your IONOS Server

**Copy and paste this exact command:**

```bash
ssh acc429003293@access946050282.webspace-data.io
```

**What you should see:**
```
The authenticity of host 'access946050282.webspace-data.io' can't be established.
Are you sure you want to continue connecting (yes/no)? 
```

**Type:** `yes` and press Enter

**Then enter your IONOS password when prompted.**

**Success looks like:**
```
Welcome to Ubuntu 20.04.3 LTS
acc429003293@access946050282:~$
```

---

## 🚀 Step 5: Install Your Darts App

**Copy and paste these commands one by one:**

```bash
# Go to your uploaded app
cd ~/darts-app

# Check if files are there
ls -la

# Make setup script executable
chmod +x setup.sh

# Run the automatic installation
./setup.sh
```

**Expected output:**
```
🎯 Darts Scorer App - IONOS Setup Script
========================================
✅ Python 3 found
📦 Creating virtual environment...
🔧 Activating virtual environment...
📥 Installing dependencies...
🗄️ Testing database connection...
✅ Database connection successful!
🚀 Setup completed successfully!
```

---

## 🎮 Step 6: Start Your Darts Scoring App

```bash
# Activate the app environment
source venv/bin/activate

# Start your darts scoring app
python src/main.py
```

**Success looks like:**
```
Successfully connected to MySQL database
Database tables created successfully
 * Serving Flask app 'main'
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://access946050282.webspace-data.io:5000
```

---

## 🌐 Step 7: Access Your Darts App

**Open Safari and go to:**
```
http://access946050282.webspace-data.io:5000
```

**🎉 Your professional darts scoring app should be running!**

---

## 🔧 Alternative Access Methods

If the above URL doesn't work, try:

### **Option A: Find Your Public IP**
```bash
# In your SSH session, find your public IP
curl ifconfig.me
```
Then access: `http://YOUR-IP-ADDRESS:5000`

### **Option B: Use Different Port**
```bash
# Stop the current app (Ctrl+C)
# Start on port 8080
python src/main.py --port 8080
```
Then access: `http://access946050282.webspace-data.io:8080`

---

## 🎯 Production Setup (Keep App Running)

**To keep your app running even when you close Terminal:**

```bash
# Install production server
pip install gunicorn

# Start in background
nohup gunicorn --bind 0.0.0.0:5000 --chdir src main:app &

# Your app now runs permanently!
```

**Access your app anytime at:** `http://access946050282.webspace-data.io:5000`

---

## 🔧 Troubleshooting Your Specific Setup

### ❌ "Permission denied" 
```bash
# Try with explicit port
ssh -p 22 acc429003293@access946050282.webspace-data.io
```

### ❌ "Connection refused"
- Double-check you're using: `access946050282.webspace-data.io`
- Make sure you're using port 22
- Verify your IONOS password

### ❌ "Database connection failed"
**Your database is pre-configured with:**
- Host: db501876797.hosting-data.io
- Database: dbs14837239
- User: dbu738581
- Password: darts@1661

### ❌ "Port 5000 blocked"
```bash
# Try port 8080 instead
python src/main.py --port 8080
```

### ❌ "Python not found"
```bash
# Install Python on your server
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

---

## ✅ Success Checklist

You know it's working when:
- ✅ Files upload successfully to your server
- ✅ SSH connection works with your credentials
- ✅ Setup script shows "Database connection successful!"
- ✅ App starts without errors
- ✅ You can access the app in Safari
- ✅ You can create players and play games
- ✅ Statistics are saved after completing games

---

## 🎮 Using Your Professional Darts App

Once running, your app includes:

### **🔐 Player Management**
- **PIN-Protected Profiles** - Secure 4-digit codes
- **Guest Mode** - Anonymous play for visitors
- **Player Selection** - Elegant profile chooser

### **🏆 Game Features**
- **501 & 301 Games** - Classic darts modes
- **Tournament Support** - Best of 3, Best of 5
- **Real-time Scoring** - Live averages and statistics
- **Celebration Overlays** - Phil Taylor for 180s!

### **📊 Statistics & Tracking**
- **Comprehensive Stats** - Win rates, averages, game history
- **Leaderboards** - Player rankings and comparisons
- **Persistent Storage** - All data saved to your MySQL database

### **🎨 Professional Design**
- **Farmhouse Loft Theme** - Warm, elegant styling
- **Mobile-Optimized** - Perfect for phones and tablets
- **Touch-Friendly** - Large buttons for easy scoring

---

## 🆘 Need Help?

**If you get stuck at any step:**

1. **Take a screenshot** of any error messages
2. **Tell me exactly which step** you're on
3. **Copy and paste** any error text you see
4. **I'll help you fix it immediately!**

**Your server details are:**
- Server: access946050282.webspace-data.io
- Username: acc429003293
- Port: 22

**Don't worry if something doesn't work perfectly the first time - we'll get your professional darts scoring app running!** 🎯

---

## 🎉 Final Result

Once everything is working, you'll have:
- **Professional darts scoring app** running on your own server
- **Persistent player profiles** and statistics
- **Tournament support** for competitive play
- **Mobile-friendly interface** for easy use
- **Secure database storage** of all game data

**Enjoy your professional darts scoring system!** 🎯🏆

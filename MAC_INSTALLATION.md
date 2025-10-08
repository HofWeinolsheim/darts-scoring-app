# 🍎 Mac Installation Guide - Darts Scoring App

**Complete step-by-step guide for Mac users with no server experience**

## 🎯 What You'll Need

From your IONOS account, you need:
- ✅ **Server IP address** (like `123.456.789.123`)
- ✅ **SSH username** (usually `root` or your account name)
- ✅ **SSH password** or SSH key
- ✅ **Database credentials** (you already have these)

## 📍 Step 1: Find Your IONOS Server Details

1. **Log into your IONOS control panel**
2. **Look for "Server" or "Hosting" section**
3. **Find your server details:**
   - Server IP address
   - SSH access credentials
   - Root or admin username

**Screenshot locations to check:**
- "Server Management" → "Access Data"
- "Hosting" → "SSH Access"
- "VPS/Dedicated Server" → "Connection Details"

---

## 💻 Step 2: Open Terminal on Your Mac

1. **Press `Cmd + Space`** (opens Spotlight)
2. **Type "Terminal"** and press Enter
3. **You'll see a black window** - this is your command line!

---

## 📁 Step 3: Download the App from GitHub

In Terminal, copy and paste these commands one by one:

```bash
# Go to your Desktop
cd ~/Desktop

# Create a folder for the app
mkdir darts-app
cd darts-app

# Download the app from GitHub
git clone https://github.com/[REPOSITORY-LINK]
cd darts-scoring-app
```

**Note:** I'll provide the exact GitHub link once the repository is created.

---

## 🔐 Step 4: Connect to Your IONOS Server

**Replace `YOUR-USERNAME` and `YOUR-SERVER-IP` with your actual details:**

```bash
ssh YOUR-USERNAME@YOUR-SERVER-IP
```

**Examples:**
```bash
ssh root@123.456.789.123
# or
ssh admin@yourdomain.com
```

**What happens:**
- You'll be asked for a password
- Type your password (you won't see characters - that's normal!)
- Press Enter

**Success looks like:**
```
Welcome to Ubuntu 20.04.3 LTS
root@your-server:~#
```

---

## 📤 Step 5: Upload Your App to the Server

**Open a NEW Terminal window** (keep the SSH one open):

```bash
# Go back to your app folder
cd ~/Desktop/darts-app/darts-scoring-app

# Upload everything to your server
scp -r . YOUR-USERNAME@YOUR-SERVER-IP:~/darts-app/
```

**This uploads all files to your server.**

---

## 🚀 Step 6: Install the App on Your Server

**Go back to your SSH Terminal window** and run:

```bash
# Go to the uploaded app
cd ~/darts-app

# Make the setup script executable
chmod +x setup.sh

# Run the automatic installation
./setup.sh
```

**What you should see:**
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

## 🎮 Step 7: Start Your Darts App

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
 * Running on http://YOUR-SERVER-IP:5000
```

---

## 🌐 Step 8: Access Your App

**Open Safari (or any browser) and go to:**
```
http://YOUR-SERVER-IP:5000
```

**Example:** `http://123.456.789.123:5000`

**🎉 You should see your beautiful darts scoring app!**

---

## 🔧 Troubleshooting

### ❌ "Permission denied" when connecting
```bash
# Try with sudo
ssh -o PreferredAuthentications=password YOUR-USERNAME@YOUR-SERVER-IP
```

### ❌ "Connection refused"
- Check your server IP address
- Make sure SSH is enabled on your IONOS server
- Try port 22: `ssh -p 22 YOUR-USERNAME@YOUR-SERVER-IP`

### ❌ "Database connection failed"
```bash
# Check your .env file
cat .env

# Make sure your database credentials are correct
```

### ❌ "Port 5000 blocked"
```bash
# Try a different port
python src/main.py --port 8080

# Then access: http://YOUR-SERVER-IP:8080
```

### ❌ "Command not found: git"
**On your Mac:**
```bash
# Install Xcode command line tools
xcode-select --install
```

**On your server:**
```bash
# Install git
sudo apt update
sudo apt install git
```

---

## 🎯 Production Setup (Optional)

**For a professional setup that stays running:**

```bash
# Install production server
pip install gunicorn

# Start with production server
gunicorn --bind 0.0.0.0:5000 --chdir src main:app --daemon

# Your app now runs in the background!
```

---

## ✅ Success Checklist

You know it's working when:
- ✅ Setup script shows "Database connection successful!"
- ✅ App starts without errors
- ✅ You can access the app in your browser
- ✅ You can create players and play games
- ✅ Statistics are saved and displayed
- ✅ Game history appears after completing games

---

## 🆘 Need Help?

**If you get stuck:**

1. **Take a screenshot** of any error messages
2. **Tell me which step** you're on
3. **Copy and paste** any error text you see
4. **I'll help you fix it!**

**Common first-time issues:**
- Wrong server IP or username
- Firewall blocking port 5000
- Database credentials not matching
- Python not installed on server

**Don't worry - we'll get it working!** 🚀

---

## 🎮 Using Your App

Once it's running:

1. **Create Players** - Add names with optional PIN protection
2. **Start Games** - Choose 301/501 and tournament modes
3. **Score Points** - Use quick buttons or manual entry
4. **View Statistics** - Check player profiles and leaderboards
5. **Enjoy!** - Professional darts scoring with celebrations

**Your app includes:**
- PIN-protected player profiles
- Guest mode for visitors
- Tournament support (Best of 3/5)
- Real-time statistics and leaderboards
- Celebration overlays for special scores
- Mobile-optimized interface
- Persistent database storage

**Have fun with your professional darts scoring system!** 🎯

# 🚀 GitHub Repository Setup - HofWeinolsheim/darts-scoring-app

**Super simple 5-minute setup to create your GitHub repository**

## 📋 What You'll Do

1. ✅ **Create GitHub repository** (2 minutes)
2. ✅ **Upload your app files** (2 minutes)  
3. ✅ **Deploy on Railway** (1 minute)
4. ✅ **Your app is live!** 🎯

---

## 🔧 Step 1: Create GitHub Repository

### **1.1: Go to GitHub**
- **Open browser** and go to **github.com**
- **Sign in** with your account (HofWeinolsheim)

### **1.2: Create New Repository**
- **Click the "+" icon** in the top-right corner
- **Select "New repository"**

### **1.3: Repository Settings**
- **Repository name:** `darts-scoring-app`
- **Description:** `Professional Darts Scoring App with Tournament Support`
- **Visibility:** ✅ **Public** (required for Railway free tier)
- **Initialize:** ❌ **Don't check any boxes** (we'll upload files)
- **Click "Create repository"**

---

## 📤 Step 2: Upload Your App Files

### **2.1: Download and Extract**
- **Download** the `darts-railway-app.zip` file I provided
- **Extract it** to your Desktop
- **You should see a `darts_backend` folder**

### **2.2: Upload to GitHub**
On your new repository page:

1. **Click "uploading an existing file"** link
2. **Drag and drop** all files from the `darts_backend` folder
3. **Or click "choose your files"** and select all files

**Files to upload:**
```
src/                    (entire folder)
requirements.txt
railway.toml
Procfile
README.md
RAILWAY_DEPLOYMENT.md
.gitignore
.env.example
```

### **2.3: Commit Files**
- **Scroll down** to "Commit changes"
- **Commit message:** `Initial commit: Railway-ready Darts Scoring App`
- **Click "Commit changes"**

---

## 🚀 Step 3: Deploy on Railway

### **3.1: Sign Up for Railway**
- **Go to railway.app**
- **Click "Login"**
- **Sign in with GitHub** (easiest option)
- **Authorize Railway** to access your repositories

### **3.2: Deploy Your App**
- **Click "New Project"**
- **Select "Deploy from GitHub repo"**
- **Find and select:** `HofWeinolsheim/darts-scoring-app`
- **Click "Deploy Now"**

### **3.3: Wait for Deployment**
Railway will automatically:
- ✅ **Detect Python Flask app**
- ✅ **Install dependencies** from requirements.txt
- ✅ **Create PostgreSQL database**
- ✅ **Set up environment variables**
- ✅ **Deploy your app** (takes 2-3 minutes)

---

## 🌐 Step 4: Access Your Live App

### **4.1: Get Your URL**
After deployment completes:
- **Railway shows your app URL**
- **Example:** `https://darts-scoring-app-production-xxxx.railway.app`
- **Click the URL** to open your live app

### **4.2: Test Your App**
Your live darts scoring app should have:
- ✅ **Beautiful farmhouse theme**
- ✅ **Player creation with PIN protection**
- ✅ **Guest mode**
- ✅ **Tournament modes**
- ✅ **Statistics and leaderboards**
- ✅ **Mobile-optimized interface**

---

## 🎯 Your Repository Structure

After upload, your repository will look like:
```
HofWeinolsheim/darts-scoring-app/
├── src/
│   ├── static/          # Frontend files
│   ├── models/          # Database code
│   ├── routes/          # API endpoints
│   └── main.py          # Flask app
├── requirements.txt     # Python dependencies
├── railway.toml         # Railway config
├── Procfile            # Deployment config
├── README.md           # Documentation
└── RAILWAY_DEPLOYMENT.md # Deployment guide
```

---

## 🔧 Troubleshooting

### ❌ "Repository creation failed"
- Make sure you're signed in to GitHub
- Try a different repository name if needed

### ❌ "File upload failed"
- Try uploading files in smaller batches
- Make sure you're uploading the contents of `darts_backend` folder, not the folder itself

### ❌ "Railway deployment failed"
- Check the build logs in Railway dashboard
- Make sure all files uploaded correctly
- Verify requirements.txt is present

---

## ✅ Success Checklist

You know it's working when:
- ✅ **GitHub repository created** at `github.com/HofWeinolsheim/darts-scoring-app`
- ✅ **All files uploaded** to GitHub
- ✅ **Railway deployment succeeds** (green checkmark)
- ✅ **App URL loads** your darts interface
- ✅ **You can create players** and play games
- ✅ **Statistics save** after completing games

---

## 🎉 Final Result

You'll have:
- ✅ **Professional darts scoring app** live on the internet
- ✅ **Custom Railway URL** you can share with anyone
- ✅ **PostgreSQL database** that saves all game data
- ✅ **Mobile-optimized** interface for phones/tablets
- ✅ **Always online** - no downtime
- ✅ **Free hosting** with Railway's $5/month credit

**Your repository:** `https://github.com/HofWeinolsheim/darts-scoring-app`
**Your live app:** `https://your-app-name.railway.app` (Railway will provide this)

---

## 🆘 Need Help?

If you get stuck at any step:
1. **Take a screenshot** of what you see
2. **Tell me which step** you're on
3. **I'll help you immediately!**

**This should take less than 10 minutes total. Let's get your darts app live!** 🚀🎯

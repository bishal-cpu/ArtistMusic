# 🚀 Quick Start - Your Personal Music Bot

## 5-Minute Setup

### Step 1: Get Your Credentials (5-10 min)
```bash
# Get from https://my.telegram.org/apps
API_ID=YOUR_API_ID
API_HASH=YOUR_API_HASH

# Get from @BotFather (/newbot)
BOT_TOKEN=YOUR_BOT_TOKEN

# Get from @userinfobot
OWNER_ID=YOUR_USER_ID

# Create a private channel, get its ID (negative number)
LOGGER_ID=-100YOUR_CHANNEL_ID

# Get free at https://mongodb.com/cloud/atlas
MONGO_DB_URI=mongodb+srv://user:pass@cluster.mongodb.net/db

# Generate with: python -m pyrogram --no-praise
STRING_SESSION=YOUR_SESSION_STRING
```

### Step 2: Edit `.env` File
```bash
# Open and fill in the .env file with your credentials
nano .env
```

Replace all `YOUR_*` placeholders with your actual values.

### Step 3: Verify Setup
```bash
# Run verification script
bash verify_setup.sh
```

You should see ✅ for all required variables.

### Step 4: Test Bot
```bash
# Install dependencies
pip install -r requirements.txt

# Start the bot
python -m Elevenyts
```

Bot should now be running! Test it on Telegram.

---

## What You Have

✅ **Working Music Bot** with:
- 🎵 YouTube Music Playback
- 🎧 Queue Management
- ⏸️ Pause/Resume/Skip Controls
- 🎛️ Admin Controls
- 📊 Statistics & Monitoring
- 🔐 User Authorization
- 🗄️ MongoDB Database

✅ **Complete Documentation**:
- `SETUP_GUIDE.md` - Detailed setup instructions
- `CUSTOMIZATION_CHECKLIST.md` - Full customization options
- `verify_setup.sh` - Setup verification script

---

## Customization

### Quick Customization
Edit `.env`:
```env
# Your support links
SUPPORT_CHANNEL=https://t.me/your_channel
SUPPORT_CHAT=https://t.me/your_group

# Your custom images
DEFAULT_THUMB=https://your-image-url.png
PING_IMG=https://your-image-url.png
START_IMG=https://your-image-url.png

# Bot behavior
DURATION_LIMIT=300      # Song length limit
QUEUE_LIMIT=30          # Max queue size
AUTO_LEAVE=True         # Leave after playing
VIDEO_PLAY=True         # Enable videos
```

### Advanced Customization
- **Messages**: Edit `Elevenyts/locales/en.json`
- **Commands**: Modify files in `Elevenyts/plugins/`
- **Branding**: Update `Readme.md` and images

---

## Deploy to Cloud

### Option 1: Render (Recommended - Free)
1. Push repo to GitHub
2. Go to https://render.com
3. Create new service → Connect GitHub repo
4. Add environment variables (copy from `.env`)
5. Deploy!

### Option 2: Heroku
```bash
heroku create your-bot-name
git push heroku main
heroku config:set $(cat .env | tr '\n' ' ')
```

### Option 3: Docker
```bash
docker build -t my-music-bot .
docker run --env-file .env my-music-bot
```

---

## Troubleshooting

**Bot doesn't respond?**
- ✅ Verify `.env` values are correct: `bash verify_setup.sh`
- ✅ Check BOT_TOKEN is active in @BotFather
- ✅ Make sure bot is not running elsewhere

**Can't play songs?**
- ✅ Verify MongoDB connection works
- ✅ Check STRING_SESSION values are valid
- ✅ Make sure bot is admin in the voice group

**Database errors?**
- ✅ Test MongoDB connection at atlas.mongodb.com
- ✅ Check whitelist allows your IP
- ✅ Verify credentials in connection string

---

## Important Security Notes

🔐 **Protect Your `.env` File**
- ✅ Never share it publicly
- ✅ Already in `.gitignore` (don't remove)
- ✅ Never commit to GitHub

🔐 **Secure Your Credentials**
- ✅ Use strong database passwords
- ✅ Rotate credentials monthly
- ✅ Use separate Telegram accounts for bot sessions

---

## Next Steps

1. **Now**: Fill in `.env` file with your credentials
2. **Test**: Run `bash verify_setup.sh` to confirm setup
3. **Run**: Start with `python -m Elevenyts`
4. **Customize**: Read `CUSTOMIZATION_CHECKLIST.md` for options
5. **Deploy**: Choose your hosting platform when ready

---

## File Structure Reference

```
/workspaces/ArtistMusic/
├── .env                          ← Your credentials (fill this!)
├── SETUP_GUIDE.md               ← Detailed setup instructions
├── CUSTOMIZATION_CHECKLIST.md   ← Full customization guide
├── verify_setup.sh              ← Verification script
├── requirements.txt             ← Python dependencies
├── config.py                    ← Bot configuration
├── Dockerfile                   ← Docker setup
├── render.yaml                  ← Render deployment config
└── Elevenyts/                   ← Bot source code
    ├── core/                    ← Core bot logic
    ├── plugins/                 ← Bot commands
    │   ├── playback-controls/   ← Play, skip, pause, etc.
    │   ├── admin-controles/     ← Admin commands
    │   ├── settings/            ← User settings
    │   ├── events/              ← Event handlers
    │   ├── information/         ← Info commands
    │   └── features/            ← Extra features
    └── helpers/                 ← Helper functions
```

---

## Commands Available

**User Commands**
- `/play [song]` - Play a song
- `/skip` - Skip current song
- `/pause` - Pause playback
- `/resume` - Resume playback
- `/queue` - Show song queue
- `/loop [off/all/one]` - Loop settings
- `/shuffle` - Shuffle queue
- `/stop` - Stop and leave
- `/ping` - Check bot latency
- `/stats` - Bot statistics

**Admin Commands**
- `/gban @user` - Global ban user
- `/ungban @user` - Remove global ban
- `/leave` - Leave voice chat
- `/broadcast` - Send message to all groups
- `/restart` - Restart bot
- `/maintenance` - Enable/disable maintenance mode

**Settings**
- `/auth` - Authorize user to control bot
- `/blacklist` - Blacklist songs/channels
- `/channelplay` - Enable channel playback

---

🎉 **You're all set!** Enjoy your personal music bot!

Questions? Check `SETUP_GUIDE.md` or `CUSTOMIZATION_CHECKLIST.md`

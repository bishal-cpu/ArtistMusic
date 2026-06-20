# 🎵 Customization Checklist - Make It Yours

Use this checklist to customize the bot to match your brand and preferences.

## Core Setup (Required to Run)

### Telegram Credentials
- [ ] Get API_ID and API_HASH from https://my.telegram.org/apps
- [ ] Get BOT_TOKEN from @BotFather
- [ ] Get your OWNER_ID from @userinfobot
- [ ] Create LOGGER_ID channel and add bot as admin
- [ ] Generate STRING_SESSION values using pyrogram
- [ ] Set up MongoDB database and get MONGO_DB_URI

### Bot Administration
- [ ] Make bot admin in logger channel
- [ ] Test adding bot to a voice chat group
- [ ] Verify bot can send and delete messages

---

## Branding & Customization (Optional but Recommended)

### Profile Images
- [ ] Create/find custom bot profile image
  - Recommended: 512x512 PNG
  - Upload to @BotFather via /setuserpic
  
- [ ] Upload custom bot description
  - Command in @BotFather: /setdescription
  - Example: "🎵 Your Personal Music Bot\n\nPlay any song from YouTube!\n\n/help for commands"

### Support Links
- [ ] Create Telegram support channel (or use existing)
  - Add to `.env` as SUPPORT_CHANNEL
  
- [ ] Create Telegram support group (or use existing)
  - Make bot admin
  - Add to `.env` as SUPPORT_CHAT

### Bot Images (Song/Command Images)
Replace these image URLs in `.env` with your own:

- [ ] **DEFAULT_THUMB** - Thumbnail shown for songs
  - Create: 320x320 PNG with your logo
  - Upload to: https://imgbb.com or https://catbox.moe
  
- [ ] **PING_IMG** - Image for /ping command
  
- [ ] **START_IMG** - Image shown when user /start bot
  
- [ ] **RADIO_IMG** - Image for radio feature

### Documentation
- [ ] Update `Readme.md` with:
  - Your bot name and description
  - Your Telegram links
  - Any custom features you added
  
- [ ] Update LICENSE with your name/organization
  
- [ ] Add your GitHub profile links

---

## Performance Optimization (Optional)

### Database Tuning
- [ ] Set `DURATION_LIMIT` based on your needs
  - Default: 300 min (5 hours)
  - YouTube: Keep between 5-30 min for fair usage
  
- [ ] Set `QUEUE_LIMIT` for your server
  - Default: 30 songs
  - Adjust based on RAM available
  
- [ ] Set `PLAYLIST_LIMIT`
  - Default: 20 songs
  - Protect against spam

### Feature Flags
- [ ] Decide: Enable `AUTO_LEAVE`?
  - True = Bot leaves after queue empty
  - False = Bot stays in voice chat
  
- [ ] Decide: Enable `THUMB_GEN`?
  - True = Custom thumbnails for each song
  - False = Use default thumbnail only
  
- [ ] Decide: Enable `VIDEO_PLAY`?
  - True = Support video playback
  - False = Audio only (less bandwidth)
  
- [ ] Set `VIDEO_MAX_HEIGHT` if video enabled
  - 480p = Lower quality, less data
  - 720p = Balanced
  - 1080p = Best quality, more data

### Security
- [ ] Set `EXCLUDED_CHATS` (optional)
  - List of group IDs where bot won't work
  - Format: "-100123456789 -100987654321"
  
- [ ] Set `EXCLUDED_USERNAMES` (optional)
  - List of usernames to block
  - Format: "spammer1 spammer2"

---

## Advanced Customization (For Developers)

### Modify Bot Commands
Edit files in `Elevenyts/plugins/`:

- [ ] **Playback Controls** - `playback-controls/`
  - Customize skip, pause, resume, seek behavior
  
- [ ] **Admin Controls** - `admin-controles/`
  - Add/modify admin-only commands
  - Customize gban (global ban) system
  
- [ ] **Settings** - `settings/`
  - Modify auth, blacklist, channel play settings

### Add Custom Features
- [ ] Create new command files in appropriate `plugins/` subdirectory
- [ ] Follow existing code patterns
- [ ] Update `plugins/__init__.py` to register new commands

### Modify Messages
Edit `Elevenyts/locales/en.json` to customize bot messages

- [ ] Change command responses
- [ ] Customize error messages
- [ ] Update help text

---

## Deployment & Testing

### Local Testing
- [ ] Run `bash verify_setup.sh` to check setup
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Start bot: `python -m Elevenyts`
- [ ] Test in a private group chat first
- [ ] Try all major commands: play, skip, pause, queue, etc.

### Deployment
Choose one:

- [ ] **Render** (Recommended - Free tier available)
  - Set up GitHub repository
  - Connect to Render
  - Add environment variables from `.env`
  
- [ ] **Heroku** (May require paid dyno)
  - Install Heroku CLI
  - Run `heroku create` and deploy
  
- [ ] **VPS** (DigitalOcean, Linode, etc.)
  - SSH into server
  - Clone repo and set up `.env`
  - Run bot with PM2/systemd for persistence
  
- [ ] **Docker** (Most portable)
  - Build: `docker build -t my-music-bot .`
  - Run: `docker run --env-file .env my-music-bot`

### Final Tests
- [ ] Bot responds to /start
- [ ] Bot can play songs via /play
- [ ] Queue system works
- [ ] Skip/pause/resume work
- [ ] Admin controls work
- [ ] Logs appear in logger channel

---

## Maintenance Checklist

### Monthly
- [ ] Check for updates in original repository
- [ ] Review MongoDB storage usage
- [ ] Check bot error logs
- [ ] Verify all features still working

### Quarterly
- [ ] Rotate database passwords
- [ ] Update dependencies: `pip install --upgrade -r requirements.txt`
- [ ] Review and clean up EXCLUDED_CHATS

### Yearly
- [ ] Regenerate STRING_SESSION values
- [ ] Review and update documentation
- [ ] Consider feature additions or improvements

---

## Common Customizations

### Example 1: Family-Friendly Bot
```env
DURATION_LIMIT=600      # 10 min max songs
QUEUE_LIMIT=50          # Allow longer queues
AUTO_LEAVE=True         # Leave when done
VIDEO_PLAY=False        # Audio only
```

### Example 2: DJ Bot (Unlimited)
```env
DURATION_LIMIT=0        # No limit (0 = unlimited)
QUEUE_LIMIT=100         # Big queues
AUTO_LEAVE=False        # Stay in chat
VIDEO_PLAY=True         # Full features
VIDEO_MAX_HEIGHT=720    # Balanced video
```

### Example 3: Light Bot (Low Resource)
```env
DURATION_LIMIT=300      # 5 min limit
QUEUE_LIMIT=15          # Small queues
AUTO_LEAVE=True         # Leave after
THUMB_GEN=False         # No thumbnails
VIDEO_PLAY=False        # Audio only
```

---

## ❓ Need Help?

1. **Setup Issues?** → Read `SETUP_GUIDE.md`
2. **Bot Not Working?** → Run `bash verify_setup.sh`
3. **Want to Modify Code?** → Check plugin files in `Elevenyts/plugins/`
4. **Deployment Help?** → Check `Dockerfile` and `render.yaml` templates

---

That's it! 🎉

Your personal music bot is now customized and ready to use!

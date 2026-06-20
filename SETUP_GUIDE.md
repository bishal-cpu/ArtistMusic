# 🎵 Setup Guide - Make ArtistMusic Bot Your Own

## Step 1: Get Telegram Credentials

### 1.1 Create Telegram App (API_ID & API_HASH)
1. Go to https://my.telegram.org/apps
2. Log in with your Telegram account
3. Fill in the application details:
   - App title: `YourBotName`
   - Short name: `yourbotname` (no spaces)
   - Platform: Select "Desktop"
4. Accept terms and create app
5. Copy **API_ID** and **API_HASH** to `.env` file

### 1.2 Create Bot Token (BOT_TOKEN)
1. Open Telegram and find **@BotFather**
2. Send `/newbot`
3. Answer the prompts:
   - Name your bot
   - Set username (must end with "bot")
4. Copy the token and add to `.env` as **BOT_TOKEN**

### 1.3 Get Your User ID (OWNER_ID)
1. Open Telegram and find **@userinfobot**
2. Send any message
3. Bot will reply with your ID
4. Add this as **OWNER_ID** in `.env`

---

## Step 2: Setup Logger Channel (LOGGER_ID)

The bot logs important messages to a private channel for debugging.

1. Create a new **Private Channel** in Telegram
2. Add your bot as admin to this channel
3. Send any message to the channel
4. Open channel settings → Copy channel link (e.g., `https://t.me/c/123456789/1`)
5. Extract the ID: Take the long number after `/c/` and add `-100` prefix
   - Example: `https://t.me/c/1234567890/1` → **-1001234567890**
6. Add to `.env` as **LOGGER_ID**

---

## Step 3: Setup Database (MONGO_DB_URI)

The bot needs a database to store user data and settings.

### Option A: MongoDB Atlas (Recommended - Free)
1. Go to https://www.mongodb.com/cloud/atlas
2. Create a free account
3. Create a new cluster
4. Go to Database → Collections → Create Database
5. Create a database user with a strong password
6. Click "Connect" → Select "Drivers" → Choose Python 3.6+
7. Copy the connection string
8. Replace `<username>`, `<password>`, and `<cluster>` with your details
9. Add to `.env` as **MONGO_DB_URI**

Example:
```
MONGO_DB_URI=mongodb+srv://myuser:mypassword@cluster0.abc123.mongodb.net/musicbot
```

---

## Step 4: Generate String Sessions (STRING_SESSION)

String sessions allow the bot to access Telegram without sharing your credentials.

### Generate on your machine:
```bash
pip install pyrogram
python -m pyrogram --no-praise
```

Follow prompts:
1. Select "2" for user account
2. Enter API_ID and API_HASH
3. Enter your phone number
4. Enter the OTP code from Telegram
5. Copy the generated session string

### Repeat for 3 sessions:
- Generate and add as **STRING_SESSION**
- Generate and add as **STRING_SESSION2**
- Generate and add as **STRING_SESSION3**

(Having 3 sessions makes the bot more stable)

---

## Step 5: Create Support Links

### Create Support Channel
1. Create a new channel for announcements
2. Copy the link: `https://t.me/yourchannelname`
3. Add as **SUPPORT_CHANNEL** in `.env`

### Create Support Chat
1. Create a new group for support discussions
2. Add the bot as admin
3. Copy the link: `https://t.me/yourgrouplname`
4. Add as **SUPPORT_CHAT** in `.env`

---

## Step 6: Customize Bot Settings

Edit these in `.env`:

| Setting | Description | Default |
|---------|-------------|---------|
| `DURATION_LIMIT` | Max song length in minutes | 300 |
| `QUEUE_LIMIT` | Max songs in queue | 30 |
| `PLAYLIST_LIMIT` | Max songs in playlist | 20 |
| `AUTO_LEAVE` | Leave voice chat when empty | False |
| `THUMB_GEN` | Generate custom thumbnails | True |
| `VIDEO_PLAY` | Enable video playback | True |
| `VIDEO_MAX_HEIGHT` | Video resolution (480-2160) | 1080 |

---

## Step 7: Custom Branding

Replace these image URLs with your own:
- **DEFAULT_THUMB**: Default thumbnail for songs
- **PING_IMG**: Image for /ping command
- **START_IMG**: Image for /start command
- **RADIO_IMG**: Image for radio feature

Upload images to https://imgbb.com or https://catbox.moe and get shareable URLs.

---

## Step 8: Make Bot Admin

For the bot to work properly in groups:

1. Create or use an existing group
2. Add your bot to the group
3. Open group settings → Administrators
4. Promote your bot with these permissions:
   - Delete messages
   - Restrict members
   - Invite users
   - Manage voice chats

---

## Step 9: Rename the Bot (Optional)

If you want to rename from "ArtistMusic" to your own brand:

1. Update bot name in BotFather: Send `/mybots` → Select bot → `/setname`
2. Update Readme.md with your branding
3. Update image references throughout

---

## Step 10: Deploy Your Bot

### Option A: Local Testing
```bash
# Install requirements
pip install -r requirements.txt

# Run the bot
python -m Elevenyts
```

### Option B: Deploy to Render
1. Push code to GitHub
2. Go to https://render.com
3. Create new service → Connect GitHub repo
4. Add environment variables from `.env`
5. Deploy!

### Option C: Deploy to Heroku
```bash
heroku login
heroku create your-bot-name
git push heroku main
heroku config:set $(cat .env | tr '\n' ' ')
```

---

## ✅ Verification Checklist

- [ ] API_ID and API_HASH added
- [ ] BOT_TOKEN added
- [ ] OWNER_ID added
- [ ] LOGGER_ID channel created and ID added
- [ ] MONGO_DB_URI added (MongoDB connected)
- [ ] STRING_SESSION (3 sessions) added
- [ ] SUPPORT_CHANNEL and SUPPORT_CHAT added
- [ ] Bot added as admin to logger channel
- [ ] Bot added as admin to testing group
- [ ] Bot name customized (optional)
- [ ] Custom images added (optional)

---

## 🆘 Troubleshooting

### Bot doesn't respond
- Check BOT_TOKEN is correct
- Verify bot is not already running elsewhere
- Check logger channel exists and bot is admin

### Can't generate songs
- Verify MONGO_DB_URI connection
- Check all 3 STRING_SESSION values are valid
- Ensure bot is admin in the voice group

### Database connection fails
- Test MongoDB connection at https://www.mongodb.com/cloud/atlas
- Check username/password in connection string
- Verify IP whitelist allows your location

---

## 📝 Important Security Notes

🔐 **NEVER:**
- Share your `.env` file
- Commit `.env` to Git
- Share your STRING_SESSION publicly
- Use weak database passwords

✅ **ALWAYS:**
- Keep `.env` in `.gitignore` (already done)
- Use strong, unique passwords
- Rotate credentials monthly
- Keep the bot updated

---

Made with ❤️ - Your Personal Music Bot!

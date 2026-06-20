#!/usr/bin/env python3
"""
Quick Setup Helper for ArtistMusic Bot
Helps generate required credentials
"""

import os
from pathlib import Path

def print_header():
    print("\n" + "="*60)
    print("🎵 ArtistMusic Bot - Setup Helper")
    print("="*60 + "\n")

def print_section(title):
    print(f"\n{'='*60}")
    print(f"📝 {title}")
    print(f"{'='*60}\n")

def main():
    print_header()
    
    env_file = Path(".env")
    if env_file.exists():
        print("✅ .env file already exists!")
        response = input("\nDo you want to update it? (y/n): ").lower()
        if response != 'y':
            print("\n✋ Setup cancelled. Your .env file is safe.")
            return
    
    # Collect credentials
    credentials = {}
    
    print_section("Step 1: Telegram API Credentials")
    print("👉 Get these from https://my.telegram.org/apps\n")
    credentials['API_ID'] = input("Enter API_ID: ").strip()
    credentials['API_HASH'] = input("Enter API_HASH: ").strip()
    
    print_section("Step 2: Bot Token")
    print("👉 Get this from @BotFather on Telegram (/newbot)\n")
    credentials['BOT_TOKEN'] = input("Enter BOT_TOKEN: ").strip()
    
    print_section("Step 3: Owner ID")
    print("👉 Get this from @userinfobot on Telegram\n")
    credentials['OWNER_ID'] = input("Enter OWNER_ID: ").strip()
    
    print_section("Step 4: Logger Channel ID")
    print("👉 Create a private channel and get its ID")
    print("   (negative number, e.g., -1001234567890)\n")
    credentials['LOGGER_ID'] = input("Enter LOGGER_ID: ").strip()
    
    print_section("Step 5: MongoDB Connection String")
    print("👉 Get free tier at https://www.mongodb.com/cloud/atlas\n")
    credentials['MONGO_DB_URI'] = input("Enter MONGO_DB_URI: ").strip()
    
    print_section("Step 6: String Sessions")
    print("👉 Generate using: python -m pyrogram --no-praise")
    print("   (You need 3 different sessions)\n")
    credentials['STRING_SESSION'] = input("Enter STRING_SESSION (1/3): ").strip()
    credentials['STRING_SESSION2'] = input("Enter STRING_SESSION (2/3): ").strip()
    credentials['STRING_SESSION3'] = input("Enter STRING_SESSION (3/3): ").strip()
    
    print_section("Step 7: Support Links (Optional)")
    print("👉 Your Telegram support channel and group\n")
    support_channel = input("Enter SUPPORT_CHANNEL (or press Enter to skip): ").strip()
    support_chat = input("Enter SUPPORT_CHAT (or press Enter to skip): ").strip()
    
    if support_channel:
        credentials['SUPPORT_CHANNEL'] = support_channel
    if support_chat:
        credentials['SUPPORT_CHAT'] = support_chat
    
    # Generate .env content
    env_content = """# ==========================================================
# ArtistMusic Bot Configuration - Auto Generated
# DO NOT SHARE THIS FILE!
# ==========================================================

# Telegram API
API_ID={API_ID}
API_HASH={API_HASH}

# Bot Token
BOT_TOKEN={BOT_TOKEN}

# Owner & Logger
OWNER_ID={OWNER_ID}
LOGGER_ID={LOGGER_ID}

# Database
MONGO_DB_URI={MONGO_DB_URI}

# String Sessions
STRING_SESSION={STRING_SESSION}
STRING_SESSION2={STRING_SESSION2}
STRING_SESSION3={STRING_SESSION3}

# Support Links
SUPPORT_CHANNEL={SUPPORT_CHANNEL}
SUPPORT_CHAT={SUPPORT_CHAT}

# Settings (Defaults)
DURATION_LIMIT=300
QUEUE_LIMIT=30
PLAYLIST_LIMIT=20
AUTO_LEAVE=False
THUMB_GEN=True
VIDEO_PLAY=True
VIDEO_MAX_HEIGHT=1080

# API (Optional)
ENABLE_API=True
ENABLE_COOKIES_FALLBACK=True
API_TIMEOUT=60
API_STREAM_TIMEOUT=300

# Images
DEFAULT_THUMB=https://files.catbox.moe/zlmv6v.png
PING_IMG=https://files.catbox.moe/zlmv6v.png
START_IMG=https://files.catbox.moe/zlmv6v.png
RADIO_IMG=https://files.catbox.moe/zlmv6v.png
""".format(**credentials)
    
    # Save .env file
    print_section("Saving Configuration")
    with open(".env", "w") as f:
        f.write(env_content)
    
    print("✅ .env file created successfully!")
    print("\n📝 Next steps:")
    print("   1. Make bot admin in logger channel")
    print("   2. Run: pip install -r requirements.txt")
    print("   3. Run: bash verify_setup.sh")
    print("   4. Run: python -m Elevenyts")
    
    print("\n📖 For more help, read QUICKSTART.md or SETUP_GUIDE.md")
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✋ Setup cancelled by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")

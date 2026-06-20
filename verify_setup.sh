#!/bin/bash
# Quick Setup Verification Script

echo "🎵 ArtistMusic Bot - Setup Verification"
echo "========================================"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ .env file not found!"
    echo "   Create .env file from template and fill in your credentials"
    exit 1
fi

echo "✅ .env file found"
echo ""

# Check required variables
REQUIRED_VARS=(
    "API_ID"
    "API_HASH"
    "BOT_TOKEN"
    "OWNER_ID"
    "LOGGER_ID"
    "MONGO_DB_URI"
    "STRING_SESSION"
)

echo "📋 Checking required environment variables:"
echo ""

MISSING_VARS=()

for var in "${REQUIRED_VARS[@]}"; do
    VALUE=$(grep "^$var=" .env | cut -d'=' -f2)
    
    if [ -z "$VALUE" ] || [[ "$VALUE" == "YOUR"* ]]; then
        echo "❌ $var - NOT SET"
        MISSING_VARS+=("$var")
    else
        # Show masked value
        if [ ${#VALUE} -gt 20 ]; then
            MASKED="${VALUE:0:10}...${VALUE: -5}"
        else
            MASKED=$VALUE
        fi
        echo "✅ $var - Set ($MASKED)"
    fi
done

echo ""
echo "========================================"

if [ ${#MISSING_VARS[@]} -eq 0 ]; then
    echo "✅ All required variables are set!"
    echo ""
    echo "Next steps:"
    echo "1. Make sure bot is admin in logger channel"
    echo "2. Run: pip install -r requirements.txt"
    echo "3. Run: python -m Elevenyts"
    exit 0
else
    echo "❌ Missing ${#MISSING_VARS[@]} variable(s):"
    for var in "${MISSING_VARS[@]}"; do
        echo "   - $var"
    done
    echo ""
    echo "📖 Read SETUP_GUIDE.md for detailed instructions"
    exit 1
fi

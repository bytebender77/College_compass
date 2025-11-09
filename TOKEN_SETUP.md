# Hugging Face Token Setup Guide

## Issue: Expired or Invalid Token

If you're seeing this error:
```
❌ API Error 401: User Access Token is expired
```

Your Hugging Face token needs to be updated.

## Quick Fix

### Step 1: Get a New Token

1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Click **"New token"** or **"Create token"**
3. Give it a name (e.g., "campus_compass")
4. Select **"Read"** permissions
5. Click **"Generate token"**
6. **Copy the token immediately** (you won't be able to see it again!)

### Step 2: Update Your .env File

1. Open or create `.env` file in the project root
2. Add or update the token:
   ```env
   HF_TOKEN=hf_your_new_token_here
   ```
3. Save the file

### Step 3: Restart the Server

```bash
# Stop the current server (Ctrl+C)
# Then restart:
python app.py
```

## Verify Your Token

Test if your token works:

```bash
python -c "
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('HF_TOKEN')
if token:
    print(f'✅ Token found: {token[:10]}...')
else:
    print('❌ No token found in .env file')
"
```

## Troubleshooting

### Token Not Working

- Make sure there are no extra spaces in your `.env` file
- Verify the token starts with `hf_`
- Check that the token has **Read** permissions
- Make sure you copied the entire token

### Still Getting 401 Errors

1. Verify the token is correct:
   ```bash
   cat .env | grep HF_TOKEN
   ```

2. Check if the token is expired:
   - Go to https://huggingface.co/settings/tokens
   - Check the expiration date of your token
   - Create a new one if expired

3. Make sure the server is reading the .env file:
   - The `.env` file should be in the project root (same directory as `app.py`)
   - Restart the server after updating `.env`

### Token Format

Your `.env` file should look like this:
```env
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Important:** 
- No quotes around the token
- No spaces before or after the `=`
- The token should start with `hf_`

## Alternative: Use Environment Variable

Instead of `.env` file, you can set it directly:

```bash
export HF_TOKEN=your_token_here
python app.py
```

## Need Help?

- Check the [Hugging Face Token Documentation](https://huggingface.co/docs/hub/security-tokens)
- Verify your token at https://huggingface.co/settings/tokens
- Make sure you're logged into the correct Hugging Face account


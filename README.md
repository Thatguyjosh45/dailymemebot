# Reddit to Instagram Meme Bot
This Python bot fetches the top meme from a specified subreddit and automatically posts it to an Instagram account with the meme's title as the caption.

# Features
Fetches the top post from a given subreddit.
Downloads the meme image from Reddit.
Posts the meme to an Instagram account with the title as the caption.
Requirements
Python 3.6 or higher
Reddit API credentials (via PRAW)
Instagram credentials (via Instabot)
Dependencies
You will need to install the following Python libraries:

PRAW (Python Reddit API Wrapper)
Instabot (Instagram automation bot)
Requests (to handle image downloads)
You can install the required dependencies by running:

bash
Copy
pip install praw instabot requests
Setup
Create a Reddit API Application
To use the Reddit API, you need to create an application and obtain the client_id, client_secret, and user_agent values from Reddit's app preferences page. Once you have these values, replace them in the script.

Login to Instagram
This bot uses the Instabot library for Instagram automation. You need to provide your Instagram username and password in the script. Make sure to keep these credentials secure.

Run the Script
You can use the main.py script to fetch the top meme from a specified subreddit and post it to Instagram. The script defaults to posting from the memes subreddit, but you can change the subreddit by modifying the code.

bash
Copy
python main.py
How It Works
Reddit Fetching: The bot uses the Reddit API (via PRAW) to get the top post from a specific subreddit.
Instagram Uploading: The bot uses the Instabot library to log into Instagram, download the image, and upload it with the meme's title as the caption.
Automation: The bot can be run at regular intervals (for example, using cron jobs) to keep posting fresh memes to your Instagram account.
Caution
Instagram Automation: Automating actions on Instagram (like posting) violates Instagram's terms of service and can result in account bans. Use this bot at your own risk.
Reddit Image Types: The bot only posts images that end in .jpg, .jpeg, .png, or .gif. Make sure the top meme post contains a suitable image.
Rate Limits: Both Reddit and Instagram have rate limits. Repeatedly running this bot in a short period could result in rate-limiting from either platform.
License

# This project is licensed under the MIT License - see the LICENSE file for details.


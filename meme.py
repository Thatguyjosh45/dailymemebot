import requests
from instabot import Bot
import praw

def get_top_meme(subreddit_name):
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                         client_secret='YOUR_CLIENT_SECRET',
                         user_agent='YOUR_USER_AGENT')

    subreddit = reddit.subreddit(subreddit_name)
    top_post = next(subreddit.top(limit=1))  # Get the top post
    
    if top_post.url.endswith(('jpg', 'jpeg', 'png', 'gif')):
        return top_post.url, top_post.title
    return None, None

def post_to_instagram(image_url, caption):
    bot = Bot()
    bot.login(username='YOUR_INSTAGRAM_USERNAME', password='YOUR_INSTAGRAM_PASSWORD')

    # Download the meme image
    response = requests.get(image_url, stream=True)
    with open('meme.jpg', 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    # Post the image with caption
    bot.upload_photo('meme.jpg', caption=caption)

    # Clean up
    bot.delete_photo('meme.jpg')

def main():
    meme_url, meme_caption = get_top_meme('memes')  # Choose subreddit
    if meme_url and meme_caption:
        post_to_instagram(meme_url, meme_caption)
    else:
        print("No suitable meme found")

if __name__ == "__main__":
    main()

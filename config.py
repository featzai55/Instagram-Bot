import os
from instaloader import Instaloader
class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    USER = os.environ.get("INSTAGRAM_USERNAME", "")
    OWNER = os.environ.get("OWNER_ID", "")
    INSTA_SESSIONFILE_ID = os.environ.get("INSTA_SESSIONFILE_ID", None)
    S = "0"
    STATUS = set(int(x) for x in (S).split())
    L=Instaloader()
    HELP="""
I can Download almost anything From your Instagram Account hehe.

<b>What Can Be Downloaded?:</b>

1. All posts of any Profile. (Both Public and Private,for private profiles you need to be a follower.)
2. All Posts from your feed(but don't try to spam).
3. Stories of any profile (Both Public and Private,for private profiles you need to be a follower.)
4. DP of any profile
5. Followers and Following List of any Profile.
6. List of followers who follows back the given username.
7. List of followers who are not following back the given username.
8. Stories of your Followers.
9. Tagged posts of any profile.
10. Your saved Posts.
11. IGTV videos.
12. Highlights from any profiles.
13. Any Public Post from Link(Post/Reels/IGTV)
I can do anything sir

<b>How to Download:</b>

Its Easy!!
But login first with /login command. 

You have two Options:

1. From Username:

Just send any instagram username.

For Example:
<code>feat.zai</code>
<code>z4iee</code>
<code>2ampillow</code>


2. From URL:

You can also sent a post link to download the post or video.



<b>Available Commands and Usage</b>

/start - To check whether I'm alive! But seriously I wanna die.
/restart - Restart me ofc (If you messed up anything use /restart to cool me down.)
/help - Shows this sh*t.
/login - ofc Login into your account.
/logout - Logout of your account.
/account - Shows the details of ur acc.

/posts <username> - Download posts of any username. Use /posts to download own posts.
Example : why should I provide you? 

/igtv <username> - Downloads igtv video even though who sees igtv videos.

/feed <number of posts to download> - Downloads posts from your feed (provide no of posts). .
Eg: <code>/feed 10</code> to download latest 10 posts from feed.

/saved <number of posts to download> - Downloads your saved posts(remember to provide no of posts). 
Example: <code>/saved 10</code> to download latest 10 saved posts.

/followers <username> - Get a list of all followers of given username.

/fans <username> - Get a list of of followees who follow back the given username.

/notfollowing <username> - Get a list of punks who don't follow back! .

/tagged <username> - Downloads all posts in which given username is tagged. 

/story <username> - Downloads all stories from given username.

/stories - Downloads all the stories of all your followers.

/highlights <username> - Downloads highlights from given username.


"""
    HOME_TEXT = """
<b>Hi ishigami here, [{}](tg://user?id={})

I work for my president to manage student council (ig) 
I will only work for my master [{}](tg://user?id={}).

Use /help to know What I can Do?</b>
"""
    HOME_TEXT_OWNER = """
<b>Hi, [{}](tg://user?id={})
I'm ishgami to manage your Instagram account.

Use /help to know what I can do for you.</b>
"""


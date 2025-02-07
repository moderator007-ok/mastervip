import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '7594440755:AAHtdnGt9YWGfp4RKynABmAdhoKEGI1ViH8')
    API_ID = int(os.environ.get("API_ID", '29554659'))
    API_HASH = os.environ.get("API_HASH", '7257d3b3192355ae71ada27cfdc3837c')
    AUTH_USER = os.environ.get('AUTH_USERS','7521176146').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    WEBHOOK = True  # Don't change this
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "ALONE🛡️"#Here You Can Change with Your Name  or any custom name or title you prefer
    PORT = int(os.environ.get('PORT', 8080))  # Default to 8000 for local testing


import os

from dotenv import load_dotenv


load_dotenv()

# Settings channel
API_ID = os.getenv("TG_API_ID")
API_HASH = os.getenv("TG_API_HASH")

# Channel for parser
CHANNEL = os.getenv("CHANNEL")
# Your channel
MY_CHANNEL = os.getenv("MY_CHANNEL")


LINK = "https://t.me/" + CHANNEL

import os
from dotenv import load_dotenv
from apiclient import discovery

load_dotenv()
api_key = os.getenv('YOUTUBE_API_KEY')

youtube = discovery.build('youtube', 'v3', developerKey=api_key)


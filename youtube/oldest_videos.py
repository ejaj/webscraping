from youtube.config import *
from datetime import datetime

# oldest video search
start_time = datetime(year=2021, month=6, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
end_time = datetime(year=2022, month=6, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')

req = youtube.search().list(
    part='snippet',
    q='machine learning',
    type='video',
    publishedAfter=start_time,
    publishedBefore=end_time,
    maxResults=50,
    key=lambda x: x['snippet']['publishedAt']
)
res = req.execute()
for item in res['items']:
    print(item['snippet']['title'], item['snippet']['publishedAt'], item['id']['videoId'])

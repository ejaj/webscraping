try:
    from youtube.config import *
except ImportError:
    raise ImportError('Configuration file not configured properly.')

# video search
req = youtube.search().list(
    q='avengers', part='snippet', type='video', maxResults=50
)
res = req.execute()
for item in res['items']:
    print(item['snippet']['title'])

# channel search
# req = youtube.search().list(
#     q='EnglishSpeakingSuccess', part='snippet', type='channel', maxResults=50
# )
# res = req.execute()
# for item in res['items']:
#     print(item['snippet']['title'])


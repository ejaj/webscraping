from youtube.config import *

# req = youtube.channels().list(
#     id='UC3O8-tKnz9VUn3sxZKyKN3w',
#     part='contentDetails'
# )
# res = req.execute()
# print(res)

# req = youtube.playlistItems().list(
#     playlistId='UU3O8-tKnz9VUn3sxZKyKN3w',
#     part='snippet',
#     maxResults=50,
#     )
# result = req.execute()
# print(result)

def get_channel_videos(channel_id):
    """
    Get a certain channel all videos.
    :param channel_id:
    :return:
    """
    req = youtube.channels().list(
        id=channel_id,
        part='contentDetails'
    )
    result = req.execute()
    playlist_id = result['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None
    while True:
        res = youtube.playlistItems().list(playlistId=playlist_id,
                                           part='snippet',
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        if next_page_token is None:
            break
    return videos
from youtube.config import *
from youtube.videos_certain_channel import get_channel_videos

videos = get_channel_videos('UC3O8-tKnz9VUn3sxZKyKN3w')


#
# res = youtube.videos().list(
#     id=videos[0]['snippet']['resourceId']['videoId'],
#     part='statistics',
# ).execute()
# print(res)

def get_videos_stats(video_ids):
    """
    Video list Id
    :param video_ids:
    :return:
    """
    stats = []
    for i in range(0, len(video_ids), 50):
        res = youtube.videos().list(id=','.join(video_ids[i:i + 50]),
                                    part='statistics').execute()
        stats += res['items']

    return stats


video_ids = list(map(lambda x: x['snippet']['resourceId']['videoId'], videos))
stats = get_videos_stats(video_ids)
for stat in stats:
    # print(stat['statistics'].get('commentCount', None))
    print(stat['id'], stat['statistics'])

# most viewed videos
# most_viewed = sorted(stats, key=lambda x:int(x['statistics']['viewCount']), reverse=True)
# print(most_viewed)
# for video in most_viewed:
#     print(video['id'], video['statistics']['viewCount'])

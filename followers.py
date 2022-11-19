# -*- coding: utf-8 -*-

import requests
import json

CHANNEL_ID = 'UCFo4kqllbcQ4nV83WCyraiw'
YOUTUBE_API_KEY = 'AxxxIzaSyAUSXeY5S3P7wkWq8Pir_YB3B2_jDURg9wxxx_replace_it_with_yours'

# Get youtube channel followers
def get_youtube_channel_followers():
    url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=' + CHANNEL_ID + '&key=' + YOUTUBE_API_KEY
    response = requests.get(url)
    data = json.loads(response.text)
    followers = data['items'][0]['statistics']['subscriberCount']
    return followers

if __name__ == '__main__':
    followers = get_youtube_channel_followers()
    print(followers)
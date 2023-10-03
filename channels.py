# -*- coding: utf-8 -*-

import requests
import json
import time

YOUTUBE_API_KEY = 'xAxIxzaSyAUSXeY5S3P7wkWq8Pir_YB3B2_jDURg9wxxx'

# Get youtube channel titles
def get_channel_title(channel_id):
    url = 'https://www.googleapis.com/youtube/v3/channels?part=snippet&id={}&key={}'.format(channel_id, YOUTUBE_API_KEY)
    r = requests.get(url)
    if r.status_code == 200:
        try :
            return json.loads(r.text)['items'][0]['snippet']['title']
        except KeyError:
            return 'Error'
    else:
        return 'Error'


if __name__ == '__main__':
    count = 0

    # read csv file and get channel id
    src = open('channels.csv', 'r')
    dest = open('channels_with_title.csv', 'w')

    # dict with channel id and title
    dict = {}

    for line in src:
        count += 1
        # skip first line
        if count == 1:
            continue

        channel_id = line.split(',')[1]
        if channel_id == '':
            continue

        print(count, channel_id)
        dict[channel_id] = get_channel_title(channel_id)
        if count % 100 == 0:
            time.sleep(3)

    # save dict to csv file
    dest.write('channel_id,channel_title\n')
    for key, value in dict.items():
        dest.write(key + ',' + value + '\n')

    src.close()
    dest.close()
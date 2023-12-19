import requests
import dotenv
import os
import datetime
import youtube_dl

dotenv.load_dotenv("credentials.env")
CLIENT_ID = os.environ.get('TOKEN_ID')
CLIENT_SECRET = os.environ.get('TOKEN_SECRET')


def get_token():
    url = 'https://id.twitch.tv/oauth2/token'

    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }

    response = requests.post(url, data=data)
    token_info = response.json()

    return token_info['access_token']


def get_categories(token):
    url = 'https://api.twitch.tv/helix/search/categories?query=just-chatting'

    headers = {
        'Authorization': f'Bearer {token}',
        'Client-Id': CLIENT_ID
    }

    response = requests.get(url, headers=headers)
    categories_info = response.json()

    print(categories_info)


def get_data(token):
    endpoint = 'https://api.twitch.tv/helix/clips'
    head = {
        'Authorization': f'Bearer {token}',
        'Client-Id': CLIENT_ID,
    }

    data = {
        'game_id': '509658',
        'started_at': (datetime.datetime.now() - datetime.timedelta(days=30)).isoformat() + 'Z',
    }

    data = requests.get(url=endpoint, headers=head, params=data)
    print(data.json())

    # return data.json()


# def save_data(data):
#     df = pandas.DataFrame(data['clips'])
#     df.to_excel('twitch_data.xlsx')


def download_video():
    video_url = "https://clips.twitch.tv/ArtsyProtectivePeppermintTBCheesePull-mEx23W-15ZNIxzZX"

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'data/twitch_clip.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


def main():
    # token = get_token()
    download_video()
    # get_categories(token)
    # get_data(token)
    # data = get_data(token)
    # save_data(data)


if __name__ == '__main__':
    main()

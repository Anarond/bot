import json
import requests

d = {}
with open("data.txt") as file:
    for line in file:
        key, *value = line.split()
        d[key] = value
# print(''.join(d['server']))

server = ''.join(d['server'])
port = ''.join(d['port'])
nickname = ''.join(d['nickname'])
channels = ''.join(d['channels'])

client_id = ''.join(d['client_id'])
client_secret = ''.join(d['client_secret'])
channel_name = ''.join(d['channel_name'])
#twitch_token1 = ''
#twitch_status = 401

def get_twitch_token(client_id, client_secret):
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials',
        'scope': 'user:read:email',
    }
    requests_token = requests.post(url, params)
    token_to_dict = json.loads(requests_token.text)
    twitch_token = token_to_dict['access_token']
    return twitch_token
#print(get_twitch_token(client_id, client_secret))

def get_twitch_status(client_id, get_twitch_token, channel_name):
    url = 'https://api.twitch.tv/helix/streams?user_login=' + channel_name
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {get_twitch_token}',
    }
    requests_status = requests.get(url, headers)
    status_to_dict = json.loads(requests_status.text)
    if status_to_dict['status'] == 401:
        return '401'
    elif len(status_to_dict['data']) < 0:
        return 'offline'
    else:
        return 'online'
#print(get_twitch_status(client_id, get_twitch_token, channel_name))

def get_twitch_data(client_id, get_twitch_token, channel_name):
    url = 'https://api.twitch.tv/helix/streams?user_login=' + channel_name
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {get_twitch_token}',
    }
    requests_status = requests.get(url, headers)
    status_to_dict = json.loads(requests_status.text)
    return status_to_dict
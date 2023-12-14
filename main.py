import json
import requests

d = {}
with open("data.txt") as file:
    for line in file:
        key, *value = line.split()
        d[key] = value

#print(''.join(d['server']))


server = ''.join(d['server'])
port = ''.join(d['port'])
nickname = ''.join(d['nickname'])
channels = ''.join(d['channels'])

client_id = ''.join(d['client_id'])
client_secret = ''.join(d['client_secret'])
channel_name = ''.join(d['channel_name'])
twitch_token1 = ''
twitch_status = 401

def twitch_token(client_id,client_secret):
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

def refresh_token(twitch_status):
    while twitch_status == 401:
        twitch_token1 = twitch_token(client_id, client_secret)
        request_channel_status = requests.get(f'https://api.twitch.tv/helix/streams?user_login={channel_name}', headers={
                'Client-ID': client_id,
            'Authorization': f'Bearer {twitch_token1}',
            })
        status_to_dict = json.loads(request_channel_status.text)
        #print(status_to_dict)
        twitch_status = status_to_dict
        return twitch_status

if twitch_status == 401:
    twitch_status = refresh_token(twitch_status)
else:
#функция чтоб войти в ирц?!?!?!? хз ваще
    print(twitch_status)

print(twitch_status)


#if  status_to_dict['status'] == 401:
#    twitch_token1 = twitch_token(client_id, client_secret)
#    #print(twitch_token1)
#else:
#    print(status_to_dict['data'])

#print(twitch_token1)
#print(request_channel_status.json())

#status_to_dict = json.loads(request_channel_status.text)
#twitch_channel_status = status_to_dict['data']
#print(twitch_channel_status)
#if len(twitch_channel_status) == 0:
#    print('Канал offline')
#else:
#    print('Канал online',twitch_channel_status[0]['title'], 'Игра на стриме:', twitch_channel_status[0]['game_name'])
import requests
import json
from _datetime import datetime

APIKEY = 'key'
APPID = 'appid'

url = "https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY={}".format(APIKEY)

def bot_reply(text):
    headers = {'Content-type': 'application/json;charset=UTF-8'}
    payload = {
        "language": "ja-JP",
        "botId": "Chatting",
        "appId": APPID,
        "voiceText": text,
        # "clientData": {
        #     "option": {
        #         "nickname": "[名前]",
        #         "nicknameY": "[呼び方(カタカナ)]",
        #         "sex": "[性別]",
        #         "birthdateY": "[誕生年]",
        #         "birthdateM": "[誕生月]",
        #         "birthdateD": "[誕生日]",
        #         "bloodtype": "[血液型]",
        #         "constellations": "[星座]",
        #         "place": "[住んでる地域]",
        #         "mode": "dialog"
        #         "t": "" # kansai：関西弁キャラ, akachan：赤ちゃんキャラ, 指定なし：デフォルトキャラ
        #     },
        # },
        #"appRecvTime": "2019-02-15 22:22:22",
        "appSendTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    # Transmission
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    data = r.json()
    # rec_time = data['serverSendTime']
    response = data['systemText']['expression']

    #print("response: %s" % response)
    return response

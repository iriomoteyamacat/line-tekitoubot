import random
import docomo_bot

def reply_text(text):
    return docomo_bot.bot_reply(text)

def reply_text_on_image():
    with open('resource/reply_on_image.txt', 'r') as f:
        texts = f.readlines()
    return random.choice(texts)

def reply_text_on_video():
    return reply_text_on_image()

def reply_random_sticker():
    packages = [1, 2, 3, 4]
    package_id = random.choice(packages)

    # botで利用可能なスタンプ： https://developers.line.biz/media/messaging-api/messages/sticker_list.pdf
    stickers = []
    if package_id == 1:
        # 1-17, 21, 100-139, 401-430
        stickers = list(range(1, 18))
        stickers.extend(range(21, 22))
        stickers.extend(range(100, 140))
        stickers.extend(range(401, 431))
    elif package_id == 2:
        # 18-20, 22-47, 140-179, 501-527
        stickers = list(range(18, 21))
        stickers.extend(range(22, 48))
        stickers.extend(range(140, 180))
        stickers.extend(range(501, 528))
    elif package_id == 3:
        # 180-259
        stickers = list(range(180, 260))
    elif package_id == 4:
        # 260-307, 601-632
        stickers = list(range(260, 308))
        stickers.extend(range(601, 633))
    
    sticker_id = random.choice(stickers)

    return (package_id, sticker_id)

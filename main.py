from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, VideoMessage, VideoSendMessage, StickerMessage, StickerSendMessage
)
import os
import bot_reply

app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def top_page():
    return "LINEで適当な返事をするbotです。\n特定のキーワードにのみ食いつきます（予定）。"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=bot_reply.reply_text(event.message.text)))

@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=bot_reply.reply_text_on_image()))

@handler.add(MessageEvent, message=VideoMessage)
def handle_video_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=bot_reply.reply_text_on_video()))

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    stickers = bot_reply.reply_random_sticker()
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(package_id = stickers[0], sticker_id = stickers[1]))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
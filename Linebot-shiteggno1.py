from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


from message import *
from new import *
from Function import *


import tempfile, os
import datetime
import time

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('R60lcR7k2nfcCzSfkRpAFkv6DoiXwJLIBf+zdR8qBfRig60rEZrAoTbWd3pLvmuwJ99ko49MPfPOSuxFy2a/ztkgz7UTbnSFb9BHMKR9viDEVCYirsPhufBz3EE6jllolMzE5DE2wMqKNWP7Xui1vQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('c2839c4ffb4dbbd01fccf115e767bccb
')

# 監聽所有來自 /callback 的 Post Request
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


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    message = TextSendMessage(text=msg)
    line_bot_api.reply_message(event.reply_token, message)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

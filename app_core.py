from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
import configparser

app = Flask(__name__)

# Line 聊天機器人基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

# 接收 Line 平台送過來的"通知"
@app.route("/callback", methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signature']

	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)


	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)


	return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
	if event.source.userid != "Udeadbeefdeadbeefdeadbeefdeadbeef":
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text=event.message.text)
		)

if __name__ == "__main__":
	app.run()
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# Line 聊天機器人基本資料
line_bot_api = LineBotApi('Fq76dRwUR0X8DQKTsDcuMYp3/Zxh/7PJ7O86CLN+3OKOjT8q2rKpyNTzPp3WQEIdzm2Gt+FNIOuPf8MTrZelH3q0LfpMUQUw4ABWqjXCKiIA8pRkmqdWZFmaaby2ROoRfCn8vtRD6U1/czy2BKBnDQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('540a6a9ee5559be55ddafe0b9a0b828d')

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
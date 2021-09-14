from app import app, WebhookHandler
from linebot.exceptions import InvalidSignatureError
import random

# Phoebe愛echo
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
	if event.source.userid != "Udeadbeefdeadbeefdeadbeefdeadbeef":
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text=event.message.text)
		)
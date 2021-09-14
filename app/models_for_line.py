from app import line_bot_api, handler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import random

# Phoebe愛唱歌
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
	if event.source.userid != "Udeadbeefdeadbeefdeadbeefdeadbeef":
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text=event.message.text)
		)
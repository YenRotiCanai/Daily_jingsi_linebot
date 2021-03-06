from app import line_bot_api, handler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from bs4 import BeautifulSoup
import requests
import urllib

def draw():

    response = requests.get("https://daily-jingsi.herokuapp.com/draw")
    soup = BeautifulSoup(response.content, "html.parser")
    souptext = soup.find('h2').getText().replace(" ","").replace("\n","")

    return souptext

@handler.add(MessageEvent, message=TextMessage)
def reply_text(event):
    text = draw()
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
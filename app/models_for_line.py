from app import line_bot_api, handler
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage

import random
import urllib
import request

def istock_isch(target):
	target = urllib.parse.quote(target)

	url = f'https://www.istockphoto.com/photos/{target}?phrase={target}&sort=mostpopular'
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0 Gecko/20100101 Firefox/73.0'}

	req = urllib.request.Request(url, headers=headers)
	page = urllib.request.urlopen(req).read()

	pattern = 'src="(https://media.*?"'
	img_list = []
	for match in re.finditer(pattern, str(page,'utf-8')):
		img_list.append(re.sub('amp;', '', match.group(1)))

	return img_list[random.randint(0, len(img_list) -1)]

# Phoebe愛唱歌
def pretty_echo(event):
    
    pretty_note = '♫♪♬'
    pretty_text = ''

    for i in event.message.text:

        pretty_text += i
        pretty_text += f" {random.choice(pretty_note)} "

    return pretty_text


@handler.add(MessageEvent, message=TextMessage)
def reply_text(event):

	if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":

		try:
			img_url = istock_isch(event.message.text)
			print(img_url)
			line_bot_api.reply_message(
				event.reply_token,
				ImageSendMessage(
					original_content_url = img_url,
					preview_image_url = img_url
				)
			)
		except:
			pretty_text = pretty_echo(event.message.text)
			line_bot_api.reply_message(
				event.reply_token,
				TextSendMessage(text=pretty_text)
			)
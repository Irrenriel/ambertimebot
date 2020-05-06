from telethon import TelegramClient, events, sync
import time
import re
import random
import os

api_id = 1209411
bot_hash = os.environ.get('BOT_API_HASH')
api_hash = str(bot_hash)

client = TelegramClient('AmberTime_bot', api_id, api_hash)

x = str(random.uniform(1,4))
y = str(random.uniform(1,4))

@client.on(events.NewMessage(chats=('🌳Терновый Куст')))
async def normal_handler(event):
	if event.message.message == '/gold':
		async with client.conversation('ChatWarsBot') as conv:
			time.sleep(float(x[0:4]))
			send1 = await conv.send_message('/ws_MYdnt')
			msg1 = await conv.get_response()
			time.sleep(float(y[0:4]))
			send2 = await conv.send_message('/ws_pUJWG')
			msg2 = await conv.get_response()

		mana1 = re.findall(r'\w*/\w+', msg1.message)
		mana2 = re.findall(r'\w*/\w+', msg2.message)

		answer = '\U0001f4b0Донат казначею:\n'
		answer += '\U0001f4d5 | [Перелить 10 монет](https://t.me/share/url?url=/ws_MYdnt_27) (15\U0001f4a7)\n'
		answer += '\U0001f4d7 | [Перелить 25 монет](https://t.me/share/url?url=/ws_MYdnt_28) (15\U0001f4a7)\n'
		answer += '\U0001f4d8 | [Перелить 50 монет](https://t.me/share/url?url=/ws_MYdnt_36) (300\U0001f4a7)\n'
		answer += '\U0001f4d9 | [Перелить 100 монет](https://t.me/share/url?url=/ws_MYdnt_12) (15\U0001f4a7)\n'
		answer += '\U0001f4d2 | [Перелить N монет](https://t.me/share/url?url=/ws_MYdnt_27) (15\U0001f4a7)\n'
		if 'Studio is закрыто.' in msg1.message:
			answer += '{@Irrenriel | Закрыто\U0001f6ab | ' + mana1[0] + '\U0001f4a7}\n\n'
		elif 'Studio is открыто.' in msg1.message:
			answer += '{@Irrenriel | Открыто\u2705 | ' + mana1[0] + '\U0001f4a7}\n\n'
		else:
			answer += '{@Irrenriel | ERROR | ' + mana1[0] + '\U0001f4a7}\n\n'
		#answer += '\U0001f510Попробовать открыть магазин:\n/sizam_otkroy\n\n'

		answer += '\U0001f4b0Донат помощ. казначея:\n'
		answer += '\U0001f4d5 | [Перелить 10 монет](https://t.me/share/url?url=/ws_pUJWG_28) (15\U0001f4a7)\n'
		answer += '\U0001f4d7 | [Перелить 25 монет](https://t.me/share/url?url=/ws_pUJWG_27) (15\U0001f4a7)\n'
		answer += '\U0001f4d8 | [Перелить 50 монет](https://t.me/share/url?url=/ws_pUJWG_p07) (10\U0001f4a7)\n'
		answer += '\U0001f4d9 | [Перелить 100 монет](https://t.me/share/url?url=/ws_pUJWG_p04) (10\U0001f4a7)\n'
		answer += '\U0001f4d2 | [Перелить N монет](https://t.me/share/url?url=/ws_pUJWG_28) (15\U0001f4a7)\n'
		if 'Lab is закрыто.' in msg2.message:
			answer += '{@Laniakeo | Закрыто\U0001f6ab | ' + mana2[0] + '\U0001f4a7}\n\n'
		elif 'Lab is открыто.' in msg2.message:
			answer += '{@Laniakeo | Открыто\u2705 | ' + mana2[0] + '\U0001f4a7}\n\n'
		else:
			answer += '{@Laniakeo | ERROR | ' + mana2[0] + '\U0001f4a7}\n'
		answer += '(ПРОБНЫЙ ТЕСТ БОТА)'

		await client.send_message('mytestgroupqwerty', answer, parse_mode = 'md')



'''
	if event.message.message == '/sizam_otkroy':
		async with client.conversation('ChatWarsBot') as conv:
			time.sleep(2)
			open_shop = await conv.send_message('/myshop_open')
			open_report = await conv.get_response()
		if "It's OPEN now." in open_report.message:
			await client.send_message('mytestgroupqwerty', 'Магазин открылся!')
		elif 'Ты сейчас занят другим приключением.'in open_report.message:
			await client.send_message('mytestgroupqwerty', 'Занят! Попробуй снова через минут 5!')
		else:
			await client.send_message('mytestgroupqwerty', 'ERROR')
'''

client.start()
client.run_until_disconnected()

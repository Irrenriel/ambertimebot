from telethon import TelegramClient, events, sync
import time
import re
import random
import os

# Подключение к Telethon клиенту
api_id = API_ID_FROM_TLGRM
api_hash = 'API_HAS_FROM_TLGRM'
client = TelegramClient('SESSION_NAME', api_id, api_hash)

# Список ID крафтов
craft_id = ['36', '37', '38']



# Режим разработки
TestMode = False



if TestMode == True:
# Чат в котором реагируют триггеры лавки
	echo_chat_id = 'My test group'
# Диалог ЛС в котором реагируют крафт-триггеры
	echo_chat_id_im = 394557686
# Чат в который приходит ответ на триггеры лавки
	chat_id = 'mytestgroupqwerty'
# Диалог ЛС в который приходит ответ на крафт-триггеры
	chat_id_im = 394557686
# Бот Chat Wars
	CW_chat_id = 265204902


else:
# Чат в котором реагируют триггеры лавки
	echo_chat_id = '🌳Терновый Куст'
# Диалог ЛС в котором реагируют крафт-триггеры
	echo_chat_id_im = 560877161
# Чат в который приходит ответ на триггеры лавки
	chat_id = 1306127576
# Диалог ЛС в который приходит ответ на крафт-триггеры
	chat_id_im = 560877161
# Бот Chat Wars
	CW_chat_id = 265204902



# Триггер перелива
@client.on(events.NewMessage(chats=(echo_chat_id)))
async def normal_handler(event):

	# Сам триггер
	if event.message.message == '/gold':
		async with client.conversation(CW_chat_id) as conv:
			time.sleep(float(str(random.uniform(1,4))[0:4]))
			send1 = await conv.send_message('/ws_MYdnt')
			msg1 = await conv.get_response()
			time.sleep(float(str(random.uniform(1,4))[0:4]))
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
		answer += '\U0001f510Попробовать открыть магазин:\n/sizam_otkroy\n\n'

		answer += '\U0001f4b0Донат помощ. казначея:\n'
		answer += '\U0001f4d5 | [Перелить 10 монет](https://t.me/share/url?url=/ws_pUJWG_28) (15\U0001f4a7)\n'
		answer += '\U0001f4d7 | [Перелить 25 монет](https://t.me/share/url?url=/ws_pUJWG_p10) (15\U0001f4a7)\n'
		answer += '\U0001f4d8 | [Перелить 50 монет](https://t.me/share/url?url=/ws_pUJWG_p07) (10\U0001f4a7)\n'
		answer += '\U0001f4d9 | [Перелить 100 монет](https://t.me/share/url?url=/ws_pUJWG_p04) (10\U0001f4a7)\n'
		answer += '\U0001f4d2 | [Перелить N монет](https://t.me/share/url?url=/ws_pUJWG_28) (15\U0001f4a7)\n'
		if 'Lab is закрыто.' in msg2.message:
			answer += '{@Laniakeo | Закрыто\U0001f6ab | ' + mana2[0] + '\U0001f4a7}\n\n'
		elif 'Lab is открыто.' in msg2.message:
			answer += '{@Laniakeo | Открыто\u2705 | ' + mana2[0] + '\U0001f4a7}\n\n'
		else:
			answer += '{@Laniakeo | ERROR | ' + mana2[0] + '\U0001f4a7}\n'

		await client.send_message(chat_id, answer, parse_mode = 'md')

	# Открыть магазин
	elif event.message.message == '/sizam_otkroy':
		async with client.conversation(CW_chat_id) as conv:
			time.sleep(2)
			open_shop = await conv.send_message('/myshop_open')
			open_report = await conv.get_response()
		if "It's OPEN now." in open_report.message:
			await client.send_message(chat_id, 'Магазин открылся!')
		elif 'Ты сейчас занят другим приключением.'in open_report.message:
			await client.send_message(chat_id, 'Занят! Попробуй снова через минут 5!')
		else:
			await client.send_message(chat_id, 'ERROR')



# Дистанционный крафт
@client.on(events.NewMessage(chats=(echo_chat_id_im)))
async def normal_handler(event):

	# Крафт ресурса, /c_id
	if event.message.message.startswith('/c_') and event.message.message[3:] in craft_id:
		async with client.conversation(CW_chat_id) as conv:
			time.sleep(float(str(random.uniform(1,4))[0:4]))
			craft_send = await conv.send_message(event.message.message)
			craft_msg = await conv.get_response()
		await client.send_message(chat_id_im, craft_msg.message)

	# Принять ресурсы, /g_receive
	elif '/g_recieve' in event.message.message:
		recieve = re.search(r'/g_receive.*')
		async with client.conversation(CW_chat_id) as conv:
			time.sleep(float(str(random.uniform(1,4))[0:4]))
			recieve_send = await conv.send_message(event.message.message)
			recieve_msg = await conv.get_response()
		await client.send_message(chat_id_im, recieve_msg.message)

client.start()
client.run_until_disconnected()
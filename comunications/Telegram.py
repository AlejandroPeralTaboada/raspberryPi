import json
import telepot
class Telegram:
    def __init__(self):
        with open('configTelegram.json') as jsonFile:
            self.data = json.load(jsonFile)
        self.token = self.data['token']
        self.bot = telepot.Bot(self.token)


    def addHandler(self):
        self.bot.message_loop(self.handle)

    def handle(self,bot, msg):

        print(msg)
        content_type, chat_type, chat_id = telepot.glance(msg)
        if (msg['text'] == '/hola'):
            bot.sendMessage(chat_id, 'hola, que tal?')
        print(content_type, chat_type, chat_id)

        if content_type == 'text':
            bot.sendMessage(chat_id, msg['text'])



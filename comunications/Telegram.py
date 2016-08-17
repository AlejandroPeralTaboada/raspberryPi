import json

import telepot


class Telegram:
    def __init__(self):
        with open('configTelegram.json') as jsonFile:
            self.data = json.load(jsonFile)
        self.token = self.data['token']
        self.defalutChatId = self.data['id']
        self.bot = telepot.Bot(self.token)

    def addHandler(self):
        self.bot.message_loop(self.handle)

    def handle(self, msg):
        print(msg)
        content_type, chat_type, chat_id = telepot.glance(msg)
        if (msg['text'] == '/hola'):
            self.bot.sendMessage(chat_id, 'hola, que tal?')
        print(content_type, chat_type, chat_id)

        if content_type == 'text':
            self.bot.sendMessage(chat_id, msg['text'])

    def notifyDefault(self, msg):
        self.bot.sendMessage(self.defalutChatId, msg)

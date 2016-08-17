import json
import telepot
class Telegram:
    def __init__(self):
        with open('configTelegram.json') as jsonFile:
            self.data = json.load(jsonFile)
        self.token = self.data['token']
        self.defalutChatId = self.data['id']
        self.bot = telepot.Bot(self.token)

    def addHandler(self,notify):
        self.bot.message_loop(self.handle)
        self.notify = notify

    def handle(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            self.notify(msg['text'])

    def notifyDefault(self,msg):
        self.bot.sendMessage(self.defalutChatId,msg)

import sys
import time
import telepot
import os

from comunications.Telegram import Telegram
from properties.Properties import Properties
from importlib import import_module

"""
$ python2.7 skeleton.py <token>
A skeleton for your telepot programs.
"""


def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return (res.replace("temp=", "").replace("'C\n", ""))


def handle(bot, msg):
    print(msg)
    print(getCPUtemperature())
    content_type, chat_type, chat_id = telepot.glance(msg)
    if (msg['text'] == '/hola'):
        bot.sendMessage(chat_id, 'hola, que tal?')
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])


def boot():
    TOKEN = '203317666:AAGVtOvfWfu_dyey7wz0367et4hWtOFiiTI'  # get token from command-line

    bot = telepot.Bot(TOKEN)
    bot.message_loop(handle)

    while 1:
        time.sleep(10)


def loadModule(moduleName):
    _temp = import_module('modules.' + moduleName)
    myclass = getattr(_temp, moduleName)
    return myclass()


def main():
    props = Properties()
    module = props.getModules()[0]
    # _temp =  import_module('modules.CpuTemperature')
    # myclass = getattr(_temp,'CpuTemperature')
    # myobject = myclass()
    myobject = loadModule(module['name'])

    print(getattr(myobject, myobject.getOperations()[0])())

    # telegram = Telegram()
    # telegram.addHandler()
    while 1:
        time.sleep(10)


if __name__ == '__main__':
    boot()

import os
import pymongo
import re

id_pattern = re.compile(r'^.\d+$')

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = os.environ.get("CHAT_BASE_TOKEN", "lskdfjsdj")
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5741250423:AAG_NPgUPrAncCRddyBoEmRr0K_5a7Uh_4I")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 7851526))
    API_HASH = os.environ.get("API_HASH", "93ba4db0ad662e558356871afe8ca6de")
    # Get these values from my.telegram.org
    # Banned Unwanted Members..
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://CapRem:CapRem@cluster0.i6qtu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    myclient = pymongo.MongoClient(str(MONGODB_URL))
    mydb = myclient["mutelist"]
    MUTEDB = mydb["words"]
    NOCAPDB = mydb["nocapdb"]
    LINKDB = mydb["linkdb"]
    WORKCHAT = mydb["workchat"]
    WORKCHAT = os.environ.get('WORKCHAT', '0').split()
    WORK_CHAT = [-1001951551775, -1002057398189]

import os
import pymongo
import re

id_pattern = re.compile(r'^.\d+$')

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = os.environ.get("CHAT_BASE_TOKEN", "lskdfjsdj")
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5120483476:AAF1GtPyOJIKYWjmytfpOyjVOiCPCaSve1s")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 7851526))
    API_HASH = os.environ.get("API_HASH", "93ba4db0ad662e558356871afe8ca6de")
    # Get these values from my.telegram.org
    # Banned Unwanted Members..
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb://mongo:6f90c0862dbfdd2c096f@suriya-troops_cap-mongo:27017/?tls=false")
    myclient = pymongo.MongoClient(str(MONGODB_URL))
    mydb = myclient["mutelist"]
    MUTEDB = mydb["words"]
    NOCAPDB = mydb["nocapdb"]
    LINKDB = mydb["linkdb"]
    WORKCHAT = mydb["workchat"]
    WORKCHAT = os.environ.get('WORKCHAT', '0').split()
    WORK_CHAT = [-1001864062112, -1002057398189, -1001951551775, -1001898212023, -1002145609723, -1002145609723, -1002523637223, -1002652414887]

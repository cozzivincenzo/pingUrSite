import urllib.request
from urllib.error import HTTPError
import time
import dotenv
import os
import asyncio
import redis
import logging
from aiogram import Bot, Dispatcher, executor, types

# Load .env file
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Connect to redis
redis = redis.Redis()

# Token retrieve from .env
API_TOKEN = os.environ["TOKEN"]
USER_ID = int(os.environ["USERID"])
WEB_URL = os.environ["URL"]

# Bot and Dispatcher init
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Function to block messages not from the user specified in .env
admin_only = lambda message: message.from_user.id != USER_ID

@dp.message_handler(admin_only, content_types=['any'])
async def handle_unwanted_users(message: types.Message):
    await bot.delete_message(message.chat.id, message.message_id)
    return


# /ping command to ping the website
@dp.message_handler(commands=['ping'])
async def send_welcome(message: types.Message):
    try:
        code = urllib.request.urlopen(WEB_URL).getcode()
        msg = "Online"
    except HTTPError as err:
        msg = "Offline - ERROR ---> " + str(err)
    await message.reply(msg)
    
    
# loop function to keep pinging the website every 60 seconds
async def check_status(sleep_for):
    while True:
        await asyncio.sleep(sleep_for)
        http_code = redis.get("http_code")
        try:
            code = urllib.request.urlopen(WEB_URL).getcode()
            if http_code != b"200":
                msg = "Guess who's back!"
                await bot.send_message(USER_ID, msg)
                redis.set("http_code", 200)
        except HTTPError as err:
            if http_code == b"200":
                msg = "That mf got offline again! - ERROR ---> " + str(err)
                await bot.send_message(USER_ID, msg)
                redis.set("http_code", str(err.code))


# loop and bot start
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(check_status(10))
    executor.start_polling(dp, skip_updates=True) 
    







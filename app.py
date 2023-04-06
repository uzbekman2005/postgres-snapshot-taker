from aiogram import Bot, Dispatcher, types, executor
from config.config import BotConfig
from database.db_main import DbController
import asyncio
import time
import os
from datetime import datetime
cfg = BotConfig(os.getenv("DOT_ENV_PATH", "config/test.env"))

bot = Bot(token=cfg.token)
dp = Dispatcher(bot)

# Define a command handler
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    if int(message.from_id) == int(cfg.admin_tg_id):
        await message.reply("Hello! I'am ready to take snapshot of your database.")
        await send_snapshots_to_admin()
    else:
        await message.reply("Hi, Using this bot is not allowed for you so you can't continue using it!!!")

# Define an echo message handler
@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer("This bot is not intended to anwser for text messages")

async def send_snapshots_to_admin():
    while True:    
        for f_n in cfg.db_files:
            await bot.send_message(int(cfg.admin_tg_id),"Snapshot of "+f_n+"\nTime:"+str(datetime.now()))
            try:
                dc = DbController(f_n+'.json', "./files/")
                dc.GetDatabaseSnapshot()
                for f in dc.res_files:
                    await bot.send_document(int(cfg.admin_tg_id), document=open("./files/"+f, "rb"))
            except Exception as ex:
                print(ex)
            finally:
                dc.DeleteSnapshotFiles()
        time.sleep(cfg.sleep_time*60)

# Start the bot
if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)   
    except Exception:
        print("Good bye")
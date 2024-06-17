import asyncio
import logging
from aiogram import Bot, Dispatcher
from Routers import routers
from dotenv import load_dotenv  # Импортируем environ 
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Настройка логгера для вывода информации в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
logger.addHandler(console_handler)

# Настройка логгера для записи информации в файл
file_handler = logging.FileHandler('bot.log')
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)

async def main():

    logger.info("Starting Bot")

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(routers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())






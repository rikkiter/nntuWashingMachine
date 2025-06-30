import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from os import getenv
from dotenv import load_dotenv

from app.handlers import router

load_dotenv()
token = getenv('BOT_TOKEN')

bot = Bot(token=token)
dp = Dispatcher()


async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
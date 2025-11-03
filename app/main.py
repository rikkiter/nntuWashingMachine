import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from app.bot.handlers import router
from app.database.database import async_main
from app.config import settings
from app.database.requests import add_machine

token = settings.BOT_TOKEN

bot = Bot(token=token)
dp = Dispatcher()


async def main() -> None:
    await async_main()
    await add_machine(5, 1)
    await add_machine(5, 2)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
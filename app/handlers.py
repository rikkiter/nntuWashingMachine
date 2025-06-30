from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboard as kb

router = Router()


@router.message(CommandStart())
async def s(message: Message) -> None:
    await message.answer("Hi")
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from app.constants import *

import app.keyboard as kb

router = Router()


@router.message(CommandStart())
async def s(message: Message) -> None:
    await message.answer(text=CHOOSE_MACHINE_INPUT_FIELD_RU, reply_markup=kb.machines)


@router.message(F.text.startswith(MACHINE_X_RU))
async def m(massage: Message) -> None:
    print(massage.text)
    await massage.answer(text="test", reply_markup=kb.machine_manager)

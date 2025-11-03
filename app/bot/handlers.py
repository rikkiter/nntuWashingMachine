from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from sqlalchemy.orm.sync import update

from app.bot.constants import *

import app.bot.keyboard as kb
from app.database.requests import get_machine, update_machine

router = Router()


class MachineId(StatesGroup):
    machine_id = State()


@router.message(CommandStart())
async def s(message: Message, state: FSMContext) -> None:
    await state.set_state(MachineId.machine_id)
    await message.answer(text=CHOOSE_MACHINE_INPUT_FIELD_RU, reply_markup=kb.machines)


@router.message(F.text.startswith(MACHINE_X_RU))
async def m(massage: Message, state: FSMContext) -> None:
    machine_id = int(massage.text.split()[-1])
    await state.update_data(machine_id=machine_id)
    data = await state.get_data()
    machine = await get_machine(5, data['machine_id'])
    await massage.answer(
        text=f"Стиральная машина {data['machine_id']} {('занята', 'свободна')[machine.status]}\nОбновлено: {machine.time}",
        reply_markup=kb.machine_manager)


@router.message(F.text == SET_BUSY_RU)
async def set_busy(massage: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await update_machine(5, data['machine_id'], 0)
    await massage.answer(f"Стиральная машина {data['machine_id']} теперь занята")


@router.message(F.text == SET_FREE_RU)
async def set_free(massage: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await update_machine(5, data['machine_id'], 1)
    await massage.answer(f"Стиральная машина {data['machine_id']} теперь свободна")


@router.message(F.text == EXIT_RU)
async def exit_to_start(message: Message, state: FSMContext) -> None:
    await s(message, state)


@router.message(Command("about"))
async def about(message: Message) -> None:
    await message.answer("text")

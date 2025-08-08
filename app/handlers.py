from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.constants import *

import app.keyboard as kb

router = Router()


class MachineId(StatesGroup):
    machine_id = State()


@router.message(CommandStart())
async def s(message: Message, state: FSMContext) -> None:
    await state.set_state(MachineId.machine_id)
    await message.answer(text=CHOOSE_MACHINE_INPUT_FIELD_RU, reply_markup=kb.machines)


@router.message(F.text.startswith(MACHINE_X_RU))
async def m(massage: Message, state: FSMContext) -> None:
    print(massage.text)
    await state.update_data(machine_id=massage.text)
    data = await state.get_data()
    await massage.answer(text=f"{data['machine_id']} свободна", reply_markup=kb.machine_manager)


@router.message(F.text == SET_BUSY_RU)
async def set_busy(massage: Message, state: FSMContext) -> None:
    s = await state.get_data()
    await massage.answer(s['machine_id'] + " теперь занята")


@router.message(F.text == SET_FREE_RU)
async def set_busy(massage: Message, state: FSMContext) -> None:
    s = await state.get_data()
    await massage.answer(s['machine_id'] + " теперь свободна")


@router.message(F.text == EXIT_RU)
async def exit_to_start(message: Message, state: FSMContext) -> None:
    await s(message, state)


@router.message(Command("about"))
async def about(message: Message) -> None:
    await message.answer("text")

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from app.bot.constants import *

machines = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=MACHINE_1_RU)],
                                         [KeyboardButton(text=MACHINE_2_RU)]],
                               resize_keyboard=True,
                               input_field_placeholder=CHOOSE_MACHINE_INPUT_FIELD_RU
                               )

machine_manager = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=SET_FREE_RU)],
                                                [KeyboardButton(text=SET_BUSY_RU)],
                                                [KeyboardButton(text=EXIT_RU)]],
                                      resize_keyboard=True,
                                      input_field_placeholder=MANAGE_MACHINE_INPUT_FIELD_RU
                                      )

from aiogram import Bot
from sqlalchemy import text

from db.manager import *
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, URLInputFile, FSInputFile
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import asyncio
import logging
import sys
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from bot.buttons.additional import contact_request_btn
from bot.buttons.reply import *
from bot.buttons.inline import *
from bot.states import *
from bot.dispatcher import dp
from environment.utils import Env
from db.engine import SessionLocal


db = SessionLocal()
admin_chat_id=Env().bot.ADMIN_CHAT_ID
bot=Bot(Env.bot.TOKEN)


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(StepByStepStates.start)
    await message.answer("Assalomu alaykum! 👋", reply_markup=ReplyKeyboardRemove())
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM users WHERE chat_id = :chat_id"), {"chat_id": message.from_user.id}).fetchone()
    if result:
        await state.set_state(StepByStepStates.main)
        btns = [
            "Restoran menyusi",
            "Biz bilan bog'lanish",
        ]
        await message.answer(
            text=f"Hush kelisbz {message.from_user.full_name}",
        )
        sizes = [1, 1]
        markup = make_reply_btn(btns, sizes)
        await message.answer("Asosiy Menyu", reply_markup=markup)
        return
    else:
        user = message.from_user
        chat_id = user.id
        fullname = user.full_name
        await state.update_data({"fullname": fullname,"chat_id":chat_id})
        await state.set_state(UserState.phone_number)
        await (message.reply("📞 Iltimos, telefon raqamingizni yuboring:", reply_markup=contact_request_btn()))

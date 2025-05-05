from aiogram import F
from aiogram.types import Message

from bot.dispatcher import dp
from bot.states import StepByStepStates


@dp.message(StepByStepStates.main,F.text=="Biz bilan bog'lanish")
async def name_handler(message:Message):
    await message.answer("Qo'ng'giroq qling!\n+998905643704")
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, CallbackQuery

from bot.buttons.inline import make_inline_btn
from bot.buttons.reply import make_reply_btn
from bot.dispatcher import dp
from bot.states import UserState, StepByStepStates


@dp.message(StepByStepStates.main,F.text=="Restoran menyusi")
async def name_handler(message:Message,state:FSMContext):
    await message.answer("Faqat tugmalardan foydalaning!", reply_markup=ReplyKeyboardRemove())
    btns=[
        "Salatlar",
        "Fast Food",
        "Issiq Taomlar",
        "Orqaga"
    ]
    sizes=[3,1]
    await state.set_state(StepByStepStates.choice_meal)
    markup=make_inline_btn(btns,sizes)
    await message.answer("Restoran Menyusi",reply_markup=markup)

@dp.callback_query(StepByStepStates.choice_meal,F.data=="Orqaga")
async def name_handler(callback:CallbackQuery,state:FSMContext):
    await callback.message.edit_text(
        text="Asosiy menyuga qaytdiz",
        reply_markup=None
    )
    await state.set_state(StepByStepStates.main)
    btns = [
        "Restoran menyusi",
        "Biz bilan bog'lanish",
    ]
    sizes = [1, 1]
    markup = make_reply_btn(btns, sizes)
    await callback.message.answer("Asosiy Menyu", reply_markup=markup)


@dp.callback_query(F.data=="Orqaga_back_menu")
async def name_handler(callback:Message,state:FSMContext):
    btns=[
        "Salatlar",
        "Fast Food",
        "Issiq Taomlar",
        "Orqaga"
    ]
    sizes=[3,1]
    await state.set_state(StepByStepStates.choice_meal)
    markup=make_inline_btn(btns,sizes)
    await callback.message.edit_text(
        text="Restoran Menyusi",
        reply_markup=markup
    )
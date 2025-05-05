from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.buttons.inline import make_inline_btn, make_inline_back_menu
from bot.dispatcher import dp
from bot.states import StepByStepStates


@dp.callback_query(StepByStepStates.choice_meal,F.data=="Issiq Taomlar")
async def name_handler(callback:CallbackQuery,state:FSMContext):
    btns=[
        "Osh",
        "Sho'rva",
        "Orqaga",
    ]
    sizes=[2,1]
    markup=make_inline_back_menu(btns,sizes,"back_menu")
    await callback.message.edit_text(
        text="Taom Tanlang:",
        reply_markup=markup
    )
    await callback.answer()
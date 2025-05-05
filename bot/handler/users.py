from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.buttons.reply import make_reply_btn
from bot.dispatcher import dp
from bot.states import UserState, StepByStepStates
from db.manager import save
from db.model import User


@dp.message(UserState.phone_number)
async def name_handler(message: Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data({"phone_number": phone_number[4:]})
    user_info = await state.get_data()
    await save(User,user_info)
    await state.clear()
    await state.set_state(StepByStepStates.main)
    btns = [
        "Restoran menyusi",
        "Biz bilan bog'lanish",
    ]
    sizes=[1,1]
    markup=make_reply_btn(btns,sizes)
    await message.answer("Asosiy Panel",reply_markup=markup)
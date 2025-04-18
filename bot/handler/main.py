from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.fsm.state import StatesGroup, State
import asyncio
import logging
import sys
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from bot.buttons.reply import *
from bot.buttons.inline import *
from bot.buttons.other_btns import *
from bot.states import *
from bot.dispatcher import dp
from db.config import *
import asyncpg
admin_chat_id=Env().bot.ADMIN_CHAT_ID
bot=Bot(Env.bot.TOKEN)
@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    if message.chat.id==admin_chat_id:
        return
    btns = [
        "👨‍💻 Developer",
        "🧑‍💼 Customer"
    ]
    sizes = [2]
    markup = make_reply_btn(btns, sizes)
    await state.set_state(StepByStepStates.level1)
    await message.answer("Who are you?", reply_markup=markup)

@dp.message(StepByStepStates.level1, F.text == "👨‍💻 Developer")
async def name_handler(message: Message, state: FSMContext):
    await state.set_state(DeveloperState.name)
    await message.answer("👋 Salom! Siz kimsiz?" )

@dp.message(DeveloperState.name, F.text)
async def name_handler(message: Message, state: FSMContext):
    name = message.text
    await state.update_data({"name": name})
    await state.set_state(DeveloperState.contact)
    await message.answer("📞 Iltimos, telefon raqamingizni yuboring:", reply_markup=contact_request_btn())

@dp.message(DeveloperState.contact)
async def name_handler(message: Message, state: FSMContext):
    contact = message.contact.phone_number
    await state.update_data({"contact": contact})
    await state.set_state(DeveloperState.occupation)
    btns = ["Backend developer", 'Frontend developer', "Fullstack developer", "Android developer"]
    sizes = [2, 2]
    markup = make_inline_btn(btns, sizes)
    await message.answer("💼 Kasbingizni tanlang:", reply_markup=markup)

# Saving developer data
@dp.callback_query(
    F.data.in_([
        "Backend developer",
        "Frontend developer",
        "Fullstack developer",
        "Android developer"
    ]), DeveloperState.occupation
)
async def bt1_handler(callback: CallbackQuery, state: FSMContext):
    occupation = callback.data
    chat_id = callback.message.chat.id
    await state.update_data({"occupation": occupation})
    await state.update_data({"chat_id": chat_id})
    developer_info = await state.get_data()
    saving_developer(developer_info)
    await callback.message.reply("✅ Ma'lumotlar saqlandi!")
    btns = [
        "📦 Ohirgi Buyurtma",
        "📂 Mening Buyurtmalarim",
        "🙋‍♂️ O'zim haqimda",
        "⚙️ Sozlamalar",
        "📞 Biz bilan bog'lanish"
    ]
    sizes = [1, 2, 2]
    markup = make_reply_btn(btns, sizes)
    await state.set_state(StepByStepStates.level2)
    await callback.message.reply("🏠 Asosiy Panelga xush kelibsiz!", reply_markup=markup)

@dp.message(StepByStepStates.level1, F.text == "🧑‍💼 Customer")
async def name_handler(message: Message, state: FSMContext):
    await state.set_state(CustomerState.name)
    await message.answer("📝 Ismingizni kiriting:")

@dp.message(CustomerState.name, F.text)
async def name_handler(message: Message, state: FSMContext):
    name = message.text
    await state.update_data({"name": name})
    await state.set_state(CustomerState.contact)
    await message.answer("📞 Iltimos, telefon raqamingizni yuboring:", reply_markup=contact_request_btn())

# Saving data customer
@dp.message(CustomerState.contact)
async def name_handler(message: Message, state: FSMContext):
    contact = message.contact.phone_number
    chat_id = message.chat.id
    await state.update_data({"contact": contact})
    await state.update_data({"chat_id": chat_id})
    customer_info = await state.get_data()
    saving_customer(customer_info)
    await message.answer("✅ Ma'lumotlar saqlandi!"  )
    btns = [
        "📝 Buyurtma berish",
        "📂 Mening Buyurtmalarim",
        "🙋‍♂️ O'zim haqimda",
        "⚙️ Sozlamalar",
        "📞 Biz bilan bog'lanish"
    ]
    sizes = [1, 2, 2]
    markup = make_reply_btn(btns, sizes)
    await state.set_state(StepByStepStates.level2)
    await message.answer("🏠 Asosiy Panelga xush kelibsiz!", reply_markup=markup)

@dp.message(StepByStepStates.level2, F.text == "📝 Buyurtma berish")
async def name_handler(message: Message, state: FSMContext):
    await state.set_state(ProjectState.name)
    await message.answer("📌 Project nomini kiriting:")

@dp.message(ProjectState.name, F.text)
async def name_handler(message: Message, state: FSMContext):
    name = message.text
    await state.update_data({"name": name})
    await state.set_state(ProjectState.description)
    await message.answer("📝 Project haqida ma'lumot kiriting:")

@dp.message(ProjectState.description, F.text)
async def name_handler(message: Message, state: FSMContext):
    description = message.text
    await state.update_data({"description": description})
    await state.set_state(ProjectState.price)
    await message.answer("💰 Narxni kiriting (so'mda):")

@dp.message(ProjectState.price, F.text.isdigit())
async def name_handler(message: Message, state: FSMContext):
    price = message.text
    await state.update_data({"price": price})
    await state.set_state(ProjectState.deadline)
    await message.answer("⏳ Muddatni kiriting (necha kunda):")

@dp.message(ProjectState.deadline, F.text.isdigit())
async def name_handler(message: Message, state: FSMContext):
    deadline = message.text
    await state.update_data({"deadline": deadline})
    await state.set_state(ProjectState.occupation)
    btns = ["backend developer", 'frontend developer', "fullstack developer", "android developer"]
    sizes = [2, 2]
    markup = make_inline_btn(btns, sizes)
    await message.answer("💼 Qaysi mutaxassis kerak?", reply_markup=markup)

@dp.callback_query(
    F.data.in_([
        "backend developer",
        "frontend developer",
        "fullstack developer",
        "android developer"
    ]), ProjectState.occupation
)
async def bt1_handler(callback: CallbackQuery, state: FSMContext):
    occupation = callback.data
    await state.update_data({"occupation": occupation})
    await state.set_state(ProjectState.tz)
    await callback.message.reply("🧾 Texnik topshiriqni (TZ) kiriting:")

# Saving Project
@dp.message(ProjectState.tz, F.text)
async def name_handler(message: Message, state: FSMContext):
    tz = message.text
    await state.update_data({"tz": tz})
    project_info = await state.get_data()
    saving_project(project_info)
    await message.answer("✅ Buyurtma saqlandi!")
    project = Project().get_all()[-1]
    msg = (
        f"🆕 Yangi Buyurtma!\n\n"
        f"📌 Nomi: {project.get('name')}\n"
        f"📄 Tavsif: {project.get('description')}\n"
        f"💰 Narx: {project.get('price')} so'm\n"
        f"⏱ Muddat: {project.get('deadline')} kun\n"
        f"🔧 Mutaxassis: {project.get('occupation')}\n"
        f"🧾 Tz: {project.get('tz')}"
    )
    btns = ["Approve","Reject"]
    sizes = [2]
    markup = make_inline_btn_confirm(btns, sizes,message.chat.id)
    await bot.send_message(chat_id=admin_chat_id,text=msg,reply_markup=markup)

@dp.callback_query(F.data.startswith("Approve"))
async def name_handler(callback: CallbackQuery, state: FSMContext):
    chat_id = int(callback.data.split('_')[1])
    await bot.send_message(chat_id=chat_id, text="✅ Admin buyurtmani tasdiqladi!")
    await callback.answer("Tasdiqlandi")
    chat_ids=set()
    project = Project().get_all()[-1]
    developer=Developer(occupation=project.get('occupation'))
    result=developer.get_all("chat_id")
    msg = (
        f"🆕 Yangi Buyurtma!\n\n"
        f"📌 Nomi: {project.get('name')}\n"
        f"📄 Tavsif: {project.get('description')}\n"
        f"💰 Narx: {project.get('price')} so'm\n"
        f"⏱ Muddat: {project.get('deadline')} kun\n"
        f"🔧 Mutaxassis: {project.get('occupation')}\n"
        f"🧾 Tz: {project.get('tz')}"
    )
    for row in result:
        if row["chat_id"] not in chat_ids:
            await bot.send_message(chat_id=row["chat_id"],text=msg)
            chat_ids.add(row["chat_id"])

@dp.callback_query(F.data.startswith("Reject"))
async def name_handler(callback: CallbackQuery, state: FSMContext):
    chat_id = int(callback.data.split('_')[1])
    await bot.send_message(chat_id=chat_id, text="❌ Admin buyurtmani tasdiqlamadi.")
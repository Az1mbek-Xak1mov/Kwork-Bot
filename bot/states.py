from aiogram.fsm.state import State, StatesGroup

class StepByStepStates(StatesGroup):
    start = State()
    main = State()
    choice_meal=State()
    settings = State()
    back_setting = State()
    back_main = State()

class UserState(StatesGroup):
    chat_id=State()
    fullname = State()
    phone_number = State()

class MealState(StatesGroup):
    name=State()
    price=State()
    count=State()

class SalatState(StatesGroup):
    name=State()
    price=State()
    count=State()

class Fast_FoodState(StatesGroup):
    name=State()
    price=State()
    count=State()

class OrderState(StatesGroup):
    chat_id=State()
    name=State()
    total_price=State()
    count=State()
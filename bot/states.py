from aiogram.fsm.state import State, StatesGroup


class StepByStepStates(StatesGroup):
    level1 = State()
    level2 = State()
    level3 = State()
    level4 = State()
    level5 = State()

class DeveloperState(StatesGroup):
    name = State()
    contact = State()
    occupation = State()
    chat_id=State()

class CustomerState(StatesGroup):
    name = State()
    contact = State()
    chat_id=State()

class ProjectState(StatesGroup):
    name = State()
    description = State()
    price = State()
    deadline = State()
    occupation = State()
    tz = State()
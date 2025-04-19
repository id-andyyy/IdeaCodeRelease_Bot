from aiogram.filters import StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage

storage: MemoryStorage = MemoryStorage()


class FSMSetGroup(StatesGroup):
    fill_action = State()
    fill_group = State()

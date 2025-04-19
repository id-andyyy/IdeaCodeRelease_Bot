from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

storage: MemoryStorage = MemoryStorage()


class FSMSetGroup(StatesGroup):
    fill_action = State()
    fill_group = State()

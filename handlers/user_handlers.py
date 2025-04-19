from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from models.methods import get_user_group, update_user_group
from states.user_states import FSMSetGroup
from keyboards.user_keyboard import create_group_keyboard
from lexicon.user_lexicon import LEXICON_USER
from lexicon.user_lexicon import LEXICON_KEYBOARDS_USER
from api.timetable_api import search_group_timetable

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_USER['/start'], reply_markup=ReplyKeyboardRemove())


@router.message(Command(commands=['group']), StateFilter(default_state))
async def process_group_command(message: Message, state: FSMContext):
    tg_id = message.from_user.id
    group_name = await get_user_group(tg_id)
    keyboard = await create_group_keyboard()
    if group_name is not None:
        await message.answer(text=LEXICON_USER['/group1'].format(group=group_name), reply_markup=keyboard)
    else:
        await message.answer(text=LEXICON_USER['/group2'], reply_markup=keyboard)
    await state.set_state(FSMSetGroup.fill_action)


@router.message(lambda message: message.text == LEXICON_KEYBOARDS_USER['change_group'], StateFilter(FSMSetGroup.fill_action))
async def process_change_group(message: Message, state: FSMContext):
    await message.answer(LEXICON_USER['/group'], reply_markup=ReplyKeyboardRemove())
    await state.set_state(FSMSetGroup.fill_group)


@router.message(StateFilter(FSMSetGroup.fill_action))
async def process_leave_group(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_USER['group_cancel'], reply_markup=ReplyKeyboardRemove())
    await state.clear()


@router.message(StateFilter(FSMSetGroup.fill_group))
async def process_fill_group(message: Message, state: FSMContext):
    group_id: int | None = await search_group_timetable(message.text)
    if group_id is not None:
        await update_user_group(message.from_user.id, message.text, group_id)
        await message.answer(text=LEXICON_USER['group_success'].format(group=message.text), reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text=LEXICON_USER['group_error'], reply_markup=ReplyKeyboardRemove())
    await state.clear()


@router.message(Command(commands=['today']))
async def process_today_command(message: Message):
    await message.answer(text=LEXICON_USER['/today'])


@router.message(Command(commands=['tomorrow']))
async def process_tomorrow_command(message: Message):
    await message.answer(text=LEXICON_USER['/tomorrow'])


@router.message(Command(commands=['timetable']))
async def process_timetable_command(message: Message):
    await message.answer(text=LEXICON_USER['/timetable'])


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_USER['/help'])

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.user_lexicon import LEXICON_KEYBOARDS_USER


async def create_group_keyboard() -> ReplyKeyboardMarkup:
    change_group_button: KeyboardButton = KeyboardButton(
        text=LEXICON_KEYBOARDS_USER['change_group'])
    leave_group_button: KeyboardButton = KeyboardButton(
        text=LEXICON_KEYBOARDS_USER['leave_group'])
    group_builder: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[[change_group_button, leave_group_button]],
        resize_keyboard=True)
    return group_builder


async def create_timetable_keyboard() -> ReplyKeyboardMarkup:
    today_button: KeyboardButton = KeyboardButton(
        text=LEXICON_KEYBOARDS_USER['today'])
    tomorrow_button: KeyboardButton = KeyboardButton(
        text=LEXICON_KEYBOARDS_USER['tomorrow'])
    timetable_button: KeyboardButton = KeyboardButton(
        text=LEXICON_KEYBOARDS_USER['timetable'])
    timetable_builder: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[[today_button, tomorrow_button], [timetable_button]],
        resize_keyboard=True)
    return timetable_builder

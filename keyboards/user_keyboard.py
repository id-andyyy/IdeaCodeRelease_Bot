from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

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

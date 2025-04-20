from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

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


async def create_week_keyboard() -> InlineKeyboardMarkup:
    weekdays = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    weekdays_upper = ['Mn_U', 'Tu_U', 'We_U', 'Th_U', 'Fr_U', 'Sa_U', 'Su_U']
    weekdays_lower = ['Mn_L', 'Tu_L', 'We_L', 'Th_L', 'Fr_L', 'Sa_L', 'Su_L']

    buttons: list[InlineKeyboardButton] = []

    for i in range(len(weekdays)):
        buttons.append(InlineKeyboardButton(
            text=weekdays[i], callback_data=weekdays_upper[i]))

    for i in range(len(weekdays)):
        buttons.append(InlineKeyboardButton(
            text=weekdays[i], callback_data=weekdays_lower[i]))

    week_builder: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[buttons[i:i + 7] for i in range(0, len(buttons), 7)])
    return week_builder

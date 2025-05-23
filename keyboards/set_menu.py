from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

from lexicon.user_lexicon import LEXICON_COMMANDS_USER


async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(
        command=command,
        description=description
    ) for command, description in LEXICON_COMMANDS_USER.items()]

    await bot.set_my_commands(commands=main_menu_commands, scope=BotCommandScopeDefault())

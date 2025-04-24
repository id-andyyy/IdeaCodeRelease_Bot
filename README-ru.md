![Арт](https://i.postimg.cc/wxnKDXKd/art-bot.png)

![GitHub Created At](https://img.shields.io/github/created-at/id-andyyy/IdeaCodeRelease_Bot?style=flat&color=00247d)
![Lines Of Code](https://tokei.rs/b1/github/id-andyyy/IdeaCodeRelease_Bot?style=flat&category=code&color=78a62d)
![Top Language](https://img.shields.io/github/languages/top/id-andyyy/IdeaCodeRelease_Bot?style=flat&color=ca4341)

# Телеграм-бот для сервиса [Твой&nbsp;ФФ&nbsp;&#127963;](https://github.com/id-andyyy/IdeaCodeRelease_Web)

Телеграм-бот Физик&nbsp;&#129302; [сервиса Твой&nbsp;ФФ](https://github.com/id-andyyy/IdeaCodeRelease_Web) для взаимодействия студентов физфака МГУ с сервисами университета&nbsp;&#128218;. Позволяет удобно просматривать расписание занятий. Создан в рамках хакатона [Идея. Код. Релиз&nbsp;&#128104;&#8205;&#128187;](https://codenrock.com/contests/codenrock-idea-code-release).

## Описание

Подробнее о самом сервисе Твой&nbsp;ФФ смотрите в [репозитории](https://github.com/id-andyyy/IdeaCodeRelease_Web). Телеграм-бот создан для удобного просмотра расписания занятий студентов и преподавателей.&nbsp;&#128104;&#8205;&#127891;

Функциональность:

- &#128142;&nbsp;Выбор группы - /group
- &#128214;&nbsp;Расписание на сегодня - /today
- &#128302;&nbsp;Расписание на завтра - /tomorrow
- &#128467;&nbsp;Всё расписание - /timetable
- &#8505;&#65039;&nbsp;Справка - /help

## Пример

Расписание отправляется в следующем формате:

```py
Расписание группы 101

Пятница, верхняя неделя

1 пара (9:00 — 10:35)
Общая астрономия
ГАИШ 48
Горбовской Е. С., Гораджанов В. С.

2 пара (10:50 — 12:25)
Молекулярная физика
5-39
Панчишин И. М.

3 пара (13:30 — 15:05)
Общая астрономия
ГАИШ 48
Сурдин В. Г.

4 пара (15:20 — 16:55)
Фтд
ГАИШ 48
Леденцов Л. С.

Сегодня воскресенье
```

Так как расписание составлено на две недели (верхняя и нижняя), студент может выбрать, день какой недели он хочет посмотреть.

## Технологии и инструменты

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffffff)
![aiogram](https://img.shields.io/badge/aiogram-005571?style=for-the-badge&color=019cfb)
![Aiohttp](https://img.shields.io/badge/aiohttp-%232C5bb4.svg?style=for-the-badge&logo=aiohttp&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white&color=f14e32)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

Проект написан за три дня в рамках хакатона [Идея. Код. Релиз&nbsp;&#128104;&#8205;&#128187;](https://codenrock.com/contests/codenrock-idea-code-release)

Backend сервиса Твой&nbsp;ФФ&nbsp;&#127963; находится в отдельном [репозитории](https://github.com/id-andyyy/IdeaCodeRelease_Web).

## Начало работы

### Настройка Backend

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&duration=2500&color=F7F7F7&background=000000&multiline=true&width=800&height=170&lines=%25+git+clone+https%3A%2F%2Fgithub.com%2Fid-andyyy%2FIdeaCodeRelease_Bot.git;%25+cd+IdeaCodeRelease_Bot;%25+python+-m+venv+venv;%25+source+venv%2Fbin%2Factivate;%25+pip+install+-r+requirements.txt;%25+python+bot.py)](https://git.io/typing-svg)

```sh
git clone https://github.com/id-andyyy/IdeaCodeRelease_Bot.git
cd IdeaCodeRelease_Bot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python bot.py
```

Для корректной работы необходимо создать файл `.env` и заполнить его в соответствии с файлом `.env.example`, заменяя заглушки секретными ключами.

## Обратная связь

Буду признателен, если вы поставите звезду&nbsp;&#11088;. Если вы нашли баг или у вас есть предложения по улучшению, используйте раздел [Issues](https://github.com/id-andyyy/IdeaCodeRelease_Bot/issues).

Читать на [английском&nbsp;&#127468;&#127463;](README.md)
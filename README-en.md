![Art](https://i.postimg.cc/wxnKDXKd/art-bot.png)

![GitHub Created At](https://img.shields.io/github/created-at/id-andyyy/IdeaCodeRelease_Bot?style=flat&color=00247d)
![](https://tokei.rs/b1/github/id-andyyy/IdeaCodeRelease_Bot?style=flat&category=code&color=78a62d)
![Top Language](https://img.shields.io/github/languages/top/id-andyyy/IdeaCodeRelease_Bot?style=flat&color=ca4341)
![Idea. Code. Release](https://img.shields.io/badge/hackathon-idea_code_release-blue?color=EDBD59)

# Telegram Bot for the Service [Твой&nbsp;ФФ&nbsp;&#127963;](https://github.com/id-andyyy/IdeaCodeRelease_Web)

Telegram Bot Fizik&nbsp;&#129302; of the [service Твой&nbsp;ФФ](https://github.com/id-andyyy/IdeaCodeRelease_Web) for interaction of MSU Physics Faculty students with university services&nbsp;&#128218;. Allows you to conveniently view the class schedule. Created as part of the hackathon [Idea. Code. Release&nbsp;&#128104;&#8205;&#128187;](https://codenrock.com/contests/codenrock-idea-code-release).

## Description

For more details about the Твой&nbsp;ФФ service, visit the [repository](https://github.com/id-andyyy/IdeaCodeRelease_Web). The Telegram bot is designed for convenient viewing of the class schedule for students and teachers.&nbsp;&#128104;&#8205;&#127891;

Functionality:

- &#128142;&nbsp;Select group - /group
- &#128214;&nbsp;Schedule for today - /today
- &#128302;&nbsp;Schedule for tomorrow - /tomorrow
- &#128467;&nbsp;Full schedule - /timetable
- &#8505;&#65039;&nbsp;Help - /help

## Example

The schedule is sent in the following format:

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

Since the schedule is made for two weeks (upper and lower), the student can choose which week's day they want to view.

## Technologies and Tools

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffffff)
![aiogram](https://img.shields.io/badge/aiogram-005571?style=for-the-badge&color=019cfb)
![Aiohttp](https://img.shields.io/badge/aiohttp-%232C5bb4.svg?style=for-the-badge&logo=aiohttp&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white&color=f14e32)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

The project was written in three days as part of the hackathon [Idea. Code. Release&nbsp;&#128104;&#8205;&#128187;](https://codenrock.com/contests/codenrock-idea-code-release)

The backend of the Your FF&nbsp;&#127963; service is located in a separate [repository](https://github.com/id-andyyy/IdeaCodeRelease_Web).

## Getting Started

### Backend Setup

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&duration=2500&color=F7F7F7&background=000000&multiline=true&width=800&height=170&lines=%25+git+clone+https%3A%2F%2Fgithub.com%2Fid-andyyy%2FIdeaCodeRelease_Bot.git;%25+cd+IdeaCodeRelease_Bot;%25+python+-m+venv+venv;%25+source+venv%2Fbin%2Factivate;%25+pip+install+-r+requirements.txt;%25+python+bot.py)](https://git.io/typing-svg)

```sh
git clone https://github.com/id-andyyy/IdeaCodeRelease_Bot.git
cd IdeaCodeRelease_Bot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python bot.py
```

To work correctly, you need to create a `.env` file and fill it in according to the `.env.example` file, replacing placeholders with secret keys.

## Feedback

I would appreciate it if you give a star&nbsp;&#11088;. If you find a bug or have suggestions for improvement, use the [Issues](https://github.com/id-andyyy/IdeaCodeRelease_Bot/issues) section.

Читать на [русском&nbsp;&#127479;&#127482;](README.md)

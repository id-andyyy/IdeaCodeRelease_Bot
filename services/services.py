from datetime import datetime, timedelta


def format_timetable(data: list[dict], group_name: str, command: str) -> str:
    months = {
        '01': 'января',
        '02': 'февраля',
        '03': 'марта',
        '04': 'апреля',
        '05': 'мая',
        '06': 'июня',
        '07': 'июля',
        '08': 'августа',
        '09': 'сентября',
        '10': 'октября',
        '11': 'ноября',
        '12': 'декабря'
    }
    weekdays = {
        0: 'понедельник',
        1: 'вторник',
        2: 'среда',
        3: 'четверг',
        4: 'пятница',
        5: 'суббота',
        6: 'воскресенье'
    }
    message = (f'Расписание группы {group_name}\n\n')

    if len(data) != 0 and "date" in data[0] and "weekday_name" in data[0]:
        date = data[0]["date"].split('.')
        message += f'{data[0]["weekday_name"].capitalize()}, {date[0]} {months[date[1]]}\n\n'
    else:
        if command == 'сегодня':
            today = datetime.now()
            message += f'{weekdays[today.weekday()].capitalize()}, {today.day} {months[today.strftime("%m")]}\n\n'
        elif command == 'завтра':
            tomorrow = datetime.now() + timedelta(days=1)
            message += f'{weekdays[tomorrow.weekday()].capitalize()}, {tomorrow.day} {months[tomorrow.strftime("%m")]}\n\n'
        else:
            weekdays_code_dict = dict(
                zip(['Mn', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'], ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']))
            week_type_dict = {
                'U': 'верхняя',
                'L': 'нижняя'
            }
            weekday_name, week_type = command.split('_')
            message += f'{weekdays_code_dict[weekday_name]}, {week_type_dict[week_type]} неделя\n\n'

    if len(data) == 0:
        message += 'Пар нет\n\n'
    else:
        for i in range(len(data)):
            message += (f'{data[i]["number"] + 1} пара ({data[i]["start_time"]} — {data[i]["end_time"]})\n'
                        f'{data[i]["subject"].capitalize()}\n')
            if len(data[i]["places"]) != 0:
                message += f'{", ".join(data[i]["places"])}\n'
            if len(data[i]["teachers"]) != 0:
                message += f'{", ".join(data[i]["teachers"])}\n'
            message += '\n'

    today_weekday = weekdays[datetime.now().weekday()]
    message += f'Сегодня {today_weekday}'

    return message

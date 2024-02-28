import locale
from datetime import datetime, timedelta


def format_date_for_chat(date_time: datetime) -> str:
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    locale.setlocale(locale.LC_TIME, 'es_ES.utf-8')
    if date_time.date() == today:
        return f'{date_time.strftime("%H:%M")}'
    elif date_time.date() == yesterday:
        return f'Ayer, {date_time.strftime("%H:%M")}'
    elif date_time.year == today.year:
        return f'{date_time.strftime("%d %B")}, {date_time.strftime("%H:%M")}'
    else:
        return f'{date_time.strftime("%d %B %Y")}, {date_time.strftime("%H:%M")}'

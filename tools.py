from datetime import date, datetime
import time
import requests

def seconds_from_start_month():
    """Возвращает время в unixtime на момент 00:00:00 первого числа месяца

    :return:
    """

    # получаем текущее время
    time_from_day_start = str(datetime.today()).split()[1].split(".")[0].split(":")

    # переводим часы в секунды
    hours_from_day_start = int(time_from_day_start[0]) * 3600

    # переводим минуты в секунды
    minutes_from_day_start = int(time_from_day_start[1]) * 60

    # секунды
    secs_from_day_start = int(time_from_day_start[2])

    # количество секунд с 00:00:00 текущего дня
    time_from_day_start_in_timestamp = int(hours_from_day_start + minutes_from_day_start + secs_from_day_start)

    # один день в секундах
    one_day = 86400

    # количество дней с начала месяца
    days_count_from_month_start = int(date.today().day) - 1

    # количество секунд до 00:00:00 первого дня месяца
    secs = one_day * days_count_from_month_start + time_from_day_start_in_timestamp

    # 00:00:00 первого дня месяца
    times = int(time.time() - secs)
    return times


def get_userid_by_username(username):
    """Получает user_id по username

    :param username: str
    :return: str(user_id)
    """
    logging_page_id = requests.get(f"https://www.instagram.com/{username}" + "/?__a=1").json()['logging_page_id']
    user_id = logging_page_id[12:len(logging_page_id)]
    return str(user_id)

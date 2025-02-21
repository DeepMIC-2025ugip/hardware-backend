from datetime import date, datetime, time


def get_day_timestamp_start_n_end(day: date) -> tuple:
    """今日の0:00:00, 23:59:59のタイムスタンプを取得"""
    start_of_day = datetime.combine(day, time.min)
    end_of_day = datetime.combine(day, time.max)

    start_timestamp = int(start_of_day.timestamp())
    end_timestamp = int(end_of_day.timestamp())

    return start_timestamp, end_timestamp

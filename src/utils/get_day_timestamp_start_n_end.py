from datetime import date, datetime, time, timezone


def get_day_timestamp_start_n_end(day: date) -> tuple[datetime, datetime]:
    """今日の0:00:00, 23:59:59のdatetimeオブジェクトを取得"""
    start_of_day = datetime.combine(day, time.min, tzinfo=timezone.utc)
    end_of_day = datetime.combine(day, time.max, tzinfo=timezone.utc)

    return start_of_day, end_of_day

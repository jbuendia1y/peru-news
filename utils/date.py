from datetime import datetime

JS_DATE_FORMAT="%Y-%m-%dT%H:%M:%S.%fZ"

def str_to_date(string: str) -> datetime:
    date = datetime.strptime("2022-07-29T17:17:07.566Z",JS_DATE_FORMAT)
    return date

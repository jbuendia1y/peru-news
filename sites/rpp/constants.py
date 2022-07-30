from datetime import datetime

CURRENT_DATE = datetime.now()

BASE_URL = "https://rpp.pe"
NEWS_PAGE = f"{BASE_URL}/archivo/{CURRENT_DATE.year}-{CURRENT_DATE.month}-{CURRENT_DATE.day}"

from datetime import datetime
from models.New import New
from sites.Page import Page


def formatter(_) -> New:
    return New("TEST IMAGE URL", "TEST TITLE", "TEST ORIGINAL URL", datetime.now())


def test_page_get_news() -> None:
    page = Page(formatter=formatter)
    news = page.get_news()
    assert news is None

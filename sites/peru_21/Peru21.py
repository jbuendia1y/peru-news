from typing import List

import requests
from models.New import New
from sites.Page import Page
from . import constants
from utils.date import str_to_date


def basic(data: dict) -> str:
    return data["url"]


def basic_jwplayer(data: dict) -> str:
    return data["embed"]["config"]["thumbnail_url"]


def basic_gallery(data: dict) -> str:
    return data["promo_items"]["basic"]["url"]


def get_image_of_promo_items(data: dict) -> str:
    basics = {
        "basic_jwplayer": basic_jwplayer,
        "basic": basic,
        "basic_gallery": basic_gallery
    }

    for key in data:
        return basics[key](data[key])


def formatter(data: dict) -> New:
    created_at = str_to_date(data["display_date"])
    title = data["headlines"]["basic"]
    original_url = constants.BASE_URL + \
        data["websites"]["peru21"]["website_url"]
    image_url = get_image_of_promo_items(data["promo_items"])

    return New(
        image_url=image_url,
        title=title,
        original_url=original_url,
        created_at=created_at
    )


class Peru21(Page):
    def __init__(self):
        super().__init__(formatter)

    def get_news(self) -> List[New]:
        req = requests.get(constants.NEWS_URL)
        data = req.json()
        news = [self.formatter(new) for new in data["content_elements"]]
        return news

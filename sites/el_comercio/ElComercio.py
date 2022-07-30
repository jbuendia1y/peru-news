import requests
from typing import List
from . import constants
from models.New import New
from sites.Page import Page
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


def format_new(data: dict) -> New:
    created_at = str_to_date(data["display_date"])
    title = data["headlines"]["basic"]
    image_url = get_image_of_promo_items(data["promo_items"])
    original_url = constants.BASE_URL + \
        data["websites"]["elcomercio"]["website_url"]

    new = New(
        title=title,
        image_url=image_url,
        original_url=original_url,
        created_at=created_at
    )
    return new


class ElComercio(Page):
    def __init__(self):
        super().__init__(
            formatter=format_new,
        )

    def get_news(self) -> List[New]:
        req = requests.get(constants.API_NEWS_URL)
        req_data = req.json()["content_elements"]
        data = [self.formatter(new) for new in req_data]
        return data

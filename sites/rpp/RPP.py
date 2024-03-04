from typing import List
from datetime import datetime

from models.New import New
from sites.Page import Page
from utils.scraper import parse_xml_from_url

import constants

BASE_URL = "https://rpp.pe"
UNPARSED_DATE_FORMAT = "%a, %d %b %Y %H:%M:%S %z"


def formatter(data: dict) -> New:
    created_at = datetime.strptime(
        data["created_at"],
        UNPARSED_DATE_FORMAT
    ).astimezone(constants.tz_utc)

    image_url = data["image_url"]
    title = data["title"]
    description = data["description"]
    original_url = data["original_url"]

    return New(
        image_url=image_url,
        title=title,
        description=description,
        original_url=original_url,
        created_at=created_at,
        website=BASE_URL
    )


class RPP(Page):
    def __init__(self):
        super().__init__(
            formatter,
        )

    def get_news(self) -> List[New]:
        d = parse_xml_from_url(BASE_URL + "/rss")
        data: List[New] = []

        for entry in d["entries"]:
            data.append(self.formatter({
                "title": entry.title,
                "description": entry.description,
                "image_url": entry.media_content[0]["url"],
                "created_at": entry.published,
                "original_url": entry.link
            }))

        return data

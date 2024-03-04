import pprint
from typing import List
from datetime import datetime

from models.New import New
from sites.Page import Page
from utils.scraper import parse_xml_from_url

import constants

BASE_URL = "https://elcomercio.pe"
UNPARSED_DATE_FORMAT = "%a, %d %b %Y %H:%M:%S %z"


def format_new(data: dict) -> New:
    image_url = data["image_url"]
    title = data["title"]
    description = data["description"]
    original_url = data["original_url"]
    created_at = datetime.strptime(
        data["created_at"],
        UNPARSED_DATE_FORMAT
    ).astimezone(constants.tz_utc)

    new = New(
        title=title,
        description=description,
        image_url=image_url,
        original_url=original_url,
        created_at=created_at,
        website=BASE_URL
    )
    return new


class ElComercio(Page):
    def __init__(self):
        super().__init__(
            formatter=format_new,
        )

    def get_news(self) -> List[New]:
        d = parse_xml_from_url(
            BASE_URL + "/arc/outboundfeeds/rss/?outputType=xml")

        data: List[New] = []

        for entry in d["entries"]:
            media_content = getattr(entry, "media_content", None)

            data.append(self.formatter({
                "title": entry.title,
                "description": entry.description,
                "created_at": entry.published,
                "original_url": entry.link,
                "image_url": media_content[0]["url"] if media_content else None
            }))

        return data

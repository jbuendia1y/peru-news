from datetime import datetime
from typing import List
from models.New import New
from sites.Page import Page
from utils.scraper import parse_xml_from_url
import constants

BASE_URL = "https://canaln.pe"
UNPARSED_DATE_FORMAT = "%a, %d %b %Y %H:%M:%S %Z"


def formatter(data: dict) -> New:
    created_at = datetime.strptime(
        data["created_at"],
        UNPARSED_DATE_FORMAT
    ).astimezone(constants.tz_utc)

    description = data["description"]
    title = data["title"]
    image_url = data["image_url"]
    original_url = data["original_url"]

    return New(
        created_at=created_at,
        description=description,
        title=title,
        image_url=image_url,
        original_url=original_url,
        website=BASE_URL
    )


class CanalN(Page):
    def __init__(self):
        super().__init__(formatter=formatter)

    def get_news(self):
        d = parse_xml_from_url(f"{BASE_URL}/feed")

        data: List[New] = []

        for entry in d["entries"]:
            data.append(self.formatter({
                "title": entry.title,
                "description": entry.description,
                "created_at": entry.published,
                "image_url": None,
                "original_url": entry.link,
            }))

        return data

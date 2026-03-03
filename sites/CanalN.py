from datetime import datetime
from typing import List

import constants
from models.New import New
from utils.scraper import parse_xml_from_url

SITENAME = "CanalN"
BASE_URL = "https://canaln.pe"
ROBOTS_URL = f"{BASE_URL}/robots.txt"
TO_SCRAP_URL = f"{BASE_URL}/feed"

UNPARSED_DATE_FORMAT = "%a, %d %b %Y %H:%M:%S %Z"


def formatter(data: dict) -> New:
    created_at = datetime.strptime(data["created_at"], UNPARSED_DATE_FORMAT).astimezone(
        constants.tz_utc
    )

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
        website=BASE_URL,
    )


async def scrap() -> List[New]:
    xml = parse_xml_from_url(TO_SCRAP_URL)

    data: List[New] = [
        formatter(
            {
                "title": entry.title,
                "description": entry.description,
                "created_at": entry.published,
                "image_url": None,
                "original_url": entry.link,
            }
        )
        for entry in xml["entries"]
    ]

    return list(data)

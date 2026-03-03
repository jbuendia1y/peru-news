from typing import List
from datetime import datetime

from models.New import New
from utils.scraper import parse_xml_from_url

import constants

SITENAME = "RPP Noticias"
BASE_URL = "https://rpp.pe"
ROBOTS_URL = f"{BASE_URL}/robots.txt"
TO_SCRAP_URL = f"{BASE_URL}/rss"

UNPARSED_DATE_FORMAT = "%a, %d %b %Y %H:%M:%S %z"


def formatter(data: dict) -> New:
    created_at = datetime.strptime(data["created_at"], UNPARSED_DATE_FORMAT).astimezone(
        constants.tz_utc
    )

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
        website=BASE_URL,
    )


async def scrap() -> List[New]:
    xml = parse_xml_from_url(TO_SCRAP_URL)

    data: List[New] = [
        formatter(
            {
                "title": entry.title,
                "description": entry.description,
                "image_url": entry.media_content[0]["url"]
                if getattr(entry, "media_content", None)
                else None,
                "created_at": entry.published,
                "original_url": entry.link,
            }
        )
        for entry in xml["entries"]
    ]

    return list(data)

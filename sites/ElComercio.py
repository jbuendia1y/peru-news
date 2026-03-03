from typing import List
from datetime import datetime

from models.New import New
from utils.scraper import parse_xml_from_url

import constants

SITENAME = "El Comercio"
BASE_URL = "https://elcomercio.pe"
ROBOTS_URL = f"{BASE_URL}/robots.txt"
TO_SCRAP_URL = f"{BASE_URL}/arc/outboundfeeds/rss/?outputType=xml"
UNPARSED_DATE_FORMAT = "%a, %d %b %Y %H:%M:%S %z"


def format_new(data: dict) -> New:
    image_url = data["image_url"]
    title = data["title"]
    description = data["description"]
    original_url = data["original_url"]
    created_at = datetime.strptime(data["created_at"], UNPARSED_DATE_FORMAT).astimezone(
        constants.tz_utc
    )

    new = New(
        title=title,
        description=description,
        image_url=image_url,
        original_url=original_url,
        created_at=created_at,
        website=BASE_URL,
    )
    return new


async def scrap() -> List[New]:
    xml = parse_xml_from_url(TO_SCRAP_URL)

    data: List[New] = []

    for entry in xml["entries"]:
        media_content = getattr(entry, "media_content", None)

        data.append(
            format_new(
                {
                    "title": entry.title,
                    "description": entry.description,
                    "created_at": entry.published,
                    "original_url": entry.link,
                    "image_url": media_content[0]["url"] if media_content else None,
                }
            )
        )

    return data

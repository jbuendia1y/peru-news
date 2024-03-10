from typing import List
import dateutil.parser as dateparser
from constants import tz_utc

from models.New import New
from sites.Page import Page

from utils.scraper import parse_xml_from_url, scrap_html_from_str

BASE_URL = "https://www.latina.pe"
RSS_URL = f"{BASE_URL}/feed"


def format_new(data: dict) -> New:
    return New(
        image_url=data["image_url"],
        title=data["title"],
        description=data["description"],
        original_url=data["original_url"],
        created_at=dateparser.parse(data["created_at"]).astimezone(tz_utc),
        website=BASE_URL,
    )


class Latina(Page):
    def __init__(self):
        super().__init__(formatter=format_new)

    def get_news(self) -> List[New]:
        d = parse_xml_from_url(RSS_URL)

        data: List[New] = []

        for entry in d["entries"]:
            soup = scrap_html_from_str(entry.description)
            html_image = soup.find("img")
            image_url = None
            if html_image:
                image_url = html_image.attrs.get("src")

            data.append(self.formatter({
                "title": entry.title,
                "description": entry.description,
                "created_at": entry.published,
                "original_url": entry.link,
                "image_url": image_url
            }))

        return data

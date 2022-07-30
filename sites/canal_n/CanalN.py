from datetime import datetime
import json
from typing import List
from bs4 import BeautifulSoup
import requests
from models.New import New
from sites.Page import Page
from . import constants


def formatter(data: dict) -> New:
    created_at = datetime.strptime(data["created_at"], constants.TIME_FORMAT)
    title = data["title"]
    image_url = data["image_url"]
    original_url = data["original_url"]

    return New(
        created_at=created_at,
        title=title,
        image_url=image_url,
        original_url=original_url,
    )


class CanalN(Page):
    def __init__(self):
        super().__init__(formatter=formatter)

    def get_news(self):
        req = requests.get(constants.NEWS_PAGE)
        html = json.loads(req.text)["noticias_html"]
        soup = BeautifulSoup(html, "lxml")
        items = soup.find_all("div", {
            "class": "nota_tab"
        })

        data: List[New] = []

        for item in items:
            """
                title = h1
                image_url = img["src"]
                original_url = a[class = ".portada-prin"]["href"]
            """
            title = item.find("span", {
                "class": "span14"
            }).text
            image_url = item.find("img")["src"]
            original_url = item.find("a", {
                "class": "crono-hover"
            })["href"]
            created_at = item.find("time").text.replace("\n", "").strip()

            new = self.formatter({
                "title": title,
                "image_url": image_url,
                "original_url": original_url,
                "created_at": created_at,
            })

            data.append(new)

        return data

import json
from typing import List

import requests
from models.New import New
from sites.Page import Page
from . import constants
import utils.scraper as scraper
from utils.date import str_to_date
from bs4 import BeautifulSoup

# .col-primary .flow-row article -> list of article
# title = h2
# image_url = figure img
# created_at = time[data-x]
# original_url = h2 a[href]


def formatter(data: dict) -> New:
    created_at = str_to_date(data["created_at"])
    image_url = data["image_url"]
    title = data["title"]
    original_url = data["original_url"]

    return New(
        image_url=image_url,
        title=title,
        original_url=original_url,
        created_at=created_at
    )


class RPP(Page):
    def __init__(self):
        super().__init__(
            formatter,
        )

    def get_news(self) -> List[New]:
        req = requests.get(constants.NEWS_PAGE)

        html = req.text
        soup = BeautifulSoup(html, "lxml")
        articles = soup.select('div[class*="flow-row"]')[0].find_all("article")

        data: List[New] = []

        for article in articles:
            title = article.find("h2").text
            min_html = json.loads(article.find(
                "figure").find("a")["data-x"])["content"]
            min_soup = BeautifulSoup(min_html, "lxml")
            image_url = min_soup.find("img")["src"]
            created_at = article.find("time")["data-x"]
            original_url = article.find("h2").find("a")["href"]

            data.append(self.formatter({
                "title": title,
                "image_url": image_url,
                "created_at": created_at,
                "original_url": original_url,
            }))

        return data

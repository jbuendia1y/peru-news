import urllib.robotparser
from typing import List

import bs4
import feedparser
import requests


def scrap_html_from_url(url: str):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    return soup


def scrap_html_from_str(value: str):
    soup = bs4.BeautifulSoup(value, "html.parser")
    return soup


def parse_xml_from_url(url: str):
    res = requests.get(url)
    xmltext = res.content
    d = feedparser.parse(xmltext)

    return d


def parse_json_from_url(url: str):
    res = requests.get(url)
    return res.json()


def check_robots(robots_url: str, site: List[str] | str) -> bool:
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()

    if type(site) is str:
        return rp.can_fetch(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36", site
        )

    for url in site:
        if not rp.can_fetch(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36", url
        ):
            return False

    return True

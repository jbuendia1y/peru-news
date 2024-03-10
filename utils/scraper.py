import requests
import feedparser
import bs4


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

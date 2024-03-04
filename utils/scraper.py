import requests
import feedparser


def parse_xml_from_url(url: str):
    res = requests.get(url)
    xmltext = res.content
    d = feedparser.parse(xmltext)

    return d


def parse_json_from_url(url: str):
    res = requests.get(url)
    return res.json()

from typing import List
from datetime import datetime

from models.New import New
from sites.Page import Page
from utils.scraper import parse_json_from_url
from constants import tz_lima, tz_utc

BASE_URL = "https://www.elperuano.pe"

NOTICIAS_DESTACADAS_URL = f"{BASE_URL}/Portal/_GetNoticiasDestacadas"
# PUBLICACIONES_OFICIALES_URL = f"{BASE_URL}/Portal/_GetNormasPortadaDiario"


def date_formatter(fecha: str):
    timestamp = int(fecha.replace("/Date(", "").replace(")/", ""))
    dt = datetime.fromtimestamp(
        timestamp / 1000, tz=tz_lima).astimezone(tz_utc)
    return dt


def format_new(data: dict):
    return New(
        title=data["title"],
        description=data["description"],
        image_url=data["image_url"],
        original_url=f"{BASE_URL}/{data['original_url']}",
        website=BASE_URL,
        created_at=date_formatter(data["created_at"])
    )


class ElPeruano(Page):
    def __init__(self):
        super().__init__(formatter=format_new)

    def get_news(self) -> List[New]:
        body = parse_json_from_url(NOTICIAS_DESTACADAS_URL)

        data: List[New] = []
        for item in body:
            data.append(self.formatter({
                "title": item["vchTitulo"],
                "description": item["vchDescripcion"],
                "image_url": item["vchRutaCompletaFotografia"],
                "original_url": item["URLFriendLy"],
                "created_at": item["dtmFecha"],
            }))
        return data

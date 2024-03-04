from dataclasses import dataclass
from datetime import datetime


@dataclass
class New:
    image_url: str | None
    title: str
    description: str
    original_url: str
    created_at: datetime

    website: str

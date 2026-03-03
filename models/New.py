from typing import Any, Dict
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

    def deserialize(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "description": self.description,
            "image_url": self.image_url,
            "original_url": self.original_url,
            "created_at": self.created_at,
            "website": self.website,
        }

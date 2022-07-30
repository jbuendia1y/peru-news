from typing import Any, Dict, List
import pandas as pd
from models.New import New
import os


class Page:
    """
        Attributes:
            - formatter (function) to format new to New dataclass
            - output_filename (str) optional filename to save all news
    """

    def __init__(self, formatter, output_filename: str = "news.csv"):
        self.formatter = formatter
        self.output_path = "datasets/" + output_filename

    def deserialize_new(self, new: New) -> Dict[str, Any]:
        return {
            "title": new.title,
            "image_url": new.image_url,
            "original_url": new.original_url,
            "created_at": new.created_at
        }

    def save_news(self, news):
        """ Save all news in datasets/news.csv """
        print("Deserialising news ...")
        data = [self.deserialize_new(new) for new in news]
        df = pd.DataFrame(data)
        print(f"Saving into {self.output_path}")
        if os.path.exists(self.output_path):
            df.to_csv(self.output_path, mode="a", header=False, index=False)
        else:
            df.to_csv(self.output_path, index=False)

    def get_news(self) -> List[New]:
        pass

    async def run(self):
        print(f"FETCHING ALL NEWS OF PAGE {self.__class__.__name__}")
        news = self.get_news()
        print("NEWS FETCHED")
        self.save_news(news)

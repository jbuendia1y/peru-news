import asyncio
import importlib
import os
import pkgutil
from typing import List

import pandas as pd

import sites
from models.New import New
from utils.scraper import check_robots

OUTPUT_DATASETS_PATH = "datasets/news.csv"


def save_news(news: List[New]):
    """Save all news in datasets/news.csv"""
    print("Deserialising news ...")

    data = [new.deserialize() for new in news]
    df = pd.DataFrame(data)
    print(f"Saving into {OUTPUT_DATASETS_PATH}")
    if os.path.exists(OUTPUT_DATASETS_PATH):
        df.to_csv(OUTPUT_DATASETS_PATH, mode="a", header=False, index=False)
    else:
        df.to_csv(OUTPUT_DATASETS_PATH, index=False)


async def scrap_site(m):
    """
    Scrap the site and save data into a file
    Arguments:
        - m: Is the module that has ROBOTS_URL, TO_SCRAP_URL and the scrap function to get news
    """
    is_valid = check_robots(m.ROBOTS_URL, m.TO_SCRAP_URL)
    if not is_valid:
        print(f"{m.SITENAME} Cannot be scrapper by the robots.txt security")
        return

    print(f"FETCHING ALL NEWS OF PAGE {m.SITENAME}")
    news = await m.scrap()
    print(f"{len(news)} NEWS FETCHED")
    save_news(news)


async def main():
    tasks = []

    print("Runing sites scraping")
    for _, module_name, _ in pkgutil.iter_modules(sites.__path__):
        module = importlib.import_module(f"sites.{module_name}")
        if hasattr(module, "scrap"):
            tasks.append(scrap_site(module))

    await asyncio.gather(*tasks)

    print("Sites scraping ends")


if __name__ == "__main__":
    asyncio.run(main())

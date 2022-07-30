from sites import sites
import asyncio
import json
from bs4 import BeautifulSoup
import requests
from sites.Page import Page
from sites.canal_n import constants


async def main():
    await sites.run()

if __name__ == "__main__":
    asyncio.run(main())

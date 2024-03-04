import asyncio
from sites import sites


async def main():
    await sites.run()

if __name__ == "__main__":
    asyncio.run(main())

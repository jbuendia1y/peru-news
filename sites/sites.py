from sites.el_comercio.ElComercio import ElComercio
from sites.rpp.RPP import RPP
from sites.canal_n.CanalN import CanalN

import asyncio


async def run():
    print("Runing sites scraping")
    await asyncio.gather(*[
        ElComercio().run(),
        RPP().run(),
        CanalN().run()
    ])
    print("Sites scraping ends")

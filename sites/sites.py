from sites.el_comercio.ElComercio import ElComercio
from sites.peru_21.Peru21 import Peru21
from sites.rpp.RPP import RPP
from sites.canal_n.CanalN import CanalN

import asyncio


async def run():
    print("Runing sites scraping")
    await asyncio.gather(*[
        ElComercio().run(),
        RPP().run(),
        CanalN().run(),
        Peru21().run()
    ])
    print("Sites scraping ends")

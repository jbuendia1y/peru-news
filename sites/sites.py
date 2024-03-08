from sites.el_comercio.ElComercio import ElComercio
from sites.rpp.RPP import RPP
from sites.canal_n.CanalN import CanalN
from sites.el_peruano.ElPeruano import ElPeruano

import asyncio


async def run():
    print("Runing sites scraping")
    await asyncio.gather(*[
        ElComercio().run(),
        RPP().run(),
        CanalN().run(),
        ElPeruano().run()
    ])
    print("Sites scraping ends")

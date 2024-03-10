from sites.el_comercio.ElComercio import ElComercio
from sites.rpp.RPP import RPP
from sites.canal_n.CanalN import CanalN
from sites.el_peruano.ElPeruano import ElPeruano
from sites.peru21.Peru21 import Peru21
from sites.latina.Latina import Latina

import asyncio


async def run():
    print("Runing sites scraping")
    await asyncio.gather(*[
        ElComercio().run(),
        RPP().run(),
        CanalN().run(),
        ElPeruano().run(),
        Peru21().run(),
        Latina().run()
    ])
    print("Sites scraping ends")

import asyncio
import logging
import time
from datetime import datetime

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()
formater = logging.Formatter('%(asctime)s:%(pathname)s <- %(funcName)s:%(levelname)s... %(message)s')
handler.setFormatter(formater)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

async def cal(x, p):
    ress = 1
    for i in range(1, p):
        logger.debug(f"calculating for {x}^{p} = {ress} <-> {i}")
        await asyncio.sleep(1)
        ress *= x
    logger.debug(f"{x}^{p} = {ress}")

if __name__ == "__main__":
    start = time.time()
    logger.info(f"start at {start}")
    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    tasks = [asyncio.ensure_future(cal(2,4)),
             asyncio.ensure_future(cal(3,10)),
             asyncio.ensure_future(cal(1,3)),
             asyncio.ensure_future(cal(3,5)),
             ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    end = time.time()
    logger.info(f"end at {end}")
    total = end - start
    logger.info(f"total time = {total}")

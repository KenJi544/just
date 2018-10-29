import asyncio
import os
import logging

import aiohttp
import async_timeout
import aiofiles


logger = logging.getLogger(name="basicasync")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('basicasync.log')
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

formatter = logging.Formatter("""%(ascitime)s - %(name)s - %(levelname)s -
                              %(messages)s""")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

async def download_coroutine(session, url):
    """ Create a coroutine to download and write to file """
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            filename = os.path.basename(url)
            print('opening file for caching')
            async with aiofiles.open('filename', mode='wb') as file:
                while True:
                    chunk = await response.content.read(1024)
                    print('awaiting byte content')
                    if not chunk:
                        print('all bytes have been read')
                        break
                    file.write(chunk)
                print('clossing file')
            print('finishing coroutine')
            return await response.release()


async def main(loop):
    """ Places all the coroutine in the loop """
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf",
           ]

    async with aiohttp.ClientSession(loop=loop) as session:
        tasks = [download_coroutine(session, url) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))

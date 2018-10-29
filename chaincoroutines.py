import asyncio


async def create():
    await asyncio.sleep(3)
    print('1. create file')


async def write():
    await asyncio.sleep(6)
    print('2. write file')


async def close():
    await asyncio.sleep(1)
    print('3. close file')


async def main(loop, *args):
    await create()
    await write()
    await close()
    await asyncio.sleep(2)
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(main(loop))
        loop.run_forever()
    except Exception as err:
        print(err)
    finally:
        loop.close()

import asyncio
from syncer import sync


async def async_fun():
    await asyncio.sleep(2)
    return 1


def syncfunc(foo):
    print(foo)

if __name__ == "__maine__":
    func = sync(async_fun)
    syncfunc(func)

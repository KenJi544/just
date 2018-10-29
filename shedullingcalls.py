import asyncio
import functools


def foo(loop, stop=False):
    print('Event handler called')
    if stop:
        print('Stopping event handler')
        loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.call_soon(foo(loop))
        print('starting event loop')
        loop.call_soon(foo(loop, stop=True))
    finally:
        print('closing event loop')
        loop.close()

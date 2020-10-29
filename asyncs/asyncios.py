import asyncio
import threading


async def async_foo():
    while True:
        print("async_foo started: ", threading.currentThread())
        await asyncio.sleep(2)
        print("async_foo done: ", threading.currentThread())


async def async_bar():
    while True:
        print("async_bar started: ", threading.currentThread())
        await asyncio.sleep(2)
        print("async_bar done: ", threading.currentThread())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(async_foo())
    asyncio.ensure_future(async_bar())

    loop.run_forever()

import asyncio


async def async_foo():
    while True:
        print("async_foo started")
        await asyncio.sleep(10)
        print("async_foo done")


async def async_bar():
    while True:
        print("async_bar started")
        await asyncio.sleep(5)
        print("async_bar done")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(async_foo())
    asyncio.ensure_future(async_bar())

    loop.run_forever()

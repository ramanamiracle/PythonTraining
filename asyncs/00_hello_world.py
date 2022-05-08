# https://docs.python.org/3/library/asyncio.html
import asyncio


async def main():  #  <-- `async` decalares an awaitable (aka coroutine)
    print("Hello ...")
    await asyncio.sleep(1)  # <--- calls an awaitable (non-blocking)
    print("... World!")


asyncio.run(main())  #  <-- initiates event loop

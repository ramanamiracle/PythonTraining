import asyncio
import time


async def sleep(seconds):
    print(f"Going to sleep... 💤")
    await asyncio.sleep(seconds)
    print(f"Slept for {seconds} seconds")


async def main():
    start = time.time()
    await sleep(1)
    await sleep(1)
    end = time.time()
    print(f"✅ Completed in {int(end-start)} seconds")


asyncio.run(main())

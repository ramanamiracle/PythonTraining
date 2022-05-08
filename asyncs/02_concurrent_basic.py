import asyncio
import time


async def sleep(seconds):
    print(f"Going to sleep... 💤")
    await asyncio.sleep(seconds)
    print(f"Slept for {seconds} seconds")


async def main():
    start = time.time()

    task_1 = asyncio.create_task(sleep(1))  # <-- task_1 is a "future"
    task_2 = asyncio.create_task(sleep(1))

    await task_1  # <-- the event loop will not block when awaiting a future
    await task_2

    end = time.time()
    print(f"✅ Completed in {int(end-start)} seconds")


asyncio.run(main())

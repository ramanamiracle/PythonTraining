import asyncio
import time

import aiohttp

NUM_TASKS = 5
SLEEP_SECONDS = 1
ENDPOINT = "https://cctv.austinmobility.io/image"
CAMERA_IDS = [100, 944, 948]


async def make_request(*, camera_id, session):
    async with session.get(f"{ENDPOINT}/{camera_id}.jpg") as response:
        return response.status


async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in CAMERA_IDS:
            task = asyncio.create_task(make_request(camera_id=i, session=session))
            tasks.append(task)

        results = await asyncio.gather(*tasks)

    end = time.time()
    for r in results:
        print(r)
    print(f"✅ Completed in {int(end-start)} seconds")


asyncio.run(main())

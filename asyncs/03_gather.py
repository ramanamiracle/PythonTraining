import asyncio
import time

NUM_TASKS = 5
SLEEP_SECONDS = 1


async def sleep(*, task_id, seconds):
    print(f"Task #{task_id} going to sleep... 💤")
    await asyncio.sleep(seconds)
    print(f"Task #{task_id} Slept for {seconds} seconds")
    return f"Result: task #{task_id} has rested 😌"


async def main():
    start = time.time()

    tasks = []
    for i in range(NUM_TASKS):
        task = asyncio.create_task(sleep(task_id=i, seconds=SLEEP_SECONDS))
        tasks.append(task)

    results = await asyncio.gather(*tasks)  # <-- send all tasks to event loop

    end = time.time()
    for r in results:
        print(r)
    print(f"✅ Completed in {int(end-start)} seconds")


asyncio.run(main())

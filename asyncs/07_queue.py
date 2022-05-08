import asyncio
import time
import random

NUM_TODOS = 10
NUM_WORKERS = 3
SLEEP_SECONDS = 1


async def worker(*, worker_id, queue):
    while True:
        try:
            # fetch the next item from the queue
            todo = await queue.get()
        except asyncio.QueueEmpty:
            # no items left - terminate worker
            break

        await asyncio.sleep(todo["sleep"])

        # make queue task as done, releasing the worker to fetch another item
        queue.task_done()
        print(f"Worker {worker_id} completed todo {todo['id']}")


async def main():
    start = time.time()

    # create our first-in/first-out queue
    queue = asyncio.Queue()

    # load simple todos into the queue
    for i in range(NUM_TODOS):
        todo = {"id": i, "sleep": random.uniform(0, 2)}
        await queue.put(todo)

    # create worker-tasks that will interact with the queue
    tasks = []
    for i in range(NUM_WORKERS):
        task = asyncio.create_task(worker(worker_id=i, queue=queue))
        tasks.append(task)

    # wait until the queue is fully processed
    await queue.join()

    # cancel our worker tasks, clearing them from memory
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)

    end = time.time()

    print(f"✅ Completed in {int(end-start)} seconds")


asyncio.run(main())

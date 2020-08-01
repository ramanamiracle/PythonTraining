import asyncio


async def mycoro(number):
    print(f"Starting :{number}")
    await asyncio.sleep(number)
    print(f"Finishing : {number}")
    return str(number)

tasks = asyncio.gather(mycoro(1), mycoro(2), mycoro(3))
loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)

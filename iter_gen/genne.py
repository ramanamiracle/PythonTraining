def coro():
    step = 0
    while True:
        print(f"started: {step}")
        received = yield step
        step += 1
        print(f"Received: {received}")


c = coro()
print(c.send(None))
print(c.send(10))

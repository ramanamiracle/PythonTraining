def coro():
    step = 1
    while True:
        print(f"started: {step}")
        print("=========before===========")
        received = yield step
        print("=========after===========")
        step += 1
        print(f"Received: {received}")
        print("=========completed===========")



c = coro()
print(c)

print(c.send(None))
print(c.send(10))
print(c.send(20))

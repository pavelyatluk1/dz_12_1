# Yatluk Pavlo
# dz_12
# 2. Написати сокет сервер з використанням бібліотеки asynsio.
# Сервер повинен приймати два числа і проводити з ними арифметичні дії -
# додавання, віднімання та мнеження з використанням користувацьких функцій
# які працюють в асинхронному режимі.

import socket
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 54500))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data1 = conn.recv(1024)
    data2 = conn.recv(1024)
    print(str(data1, data2))

    async def gr1():
        await asyncio.sleep(2)
        print(data1 + data2)

    async def gr2():
        await asyncio.sleep(2)
        print(data1 - data2)

    async def gr3():
        await asyncio.sleep(1)
        print(data1 * data2)

    ioloop = asyncio.get_event_loop()
    tasks = [
        ioloop.create_task(gr1()),
        ioloop.create_task(gr2()),
        ioloop.create_task(gr3())
    ]
    ioloop.run_until_complete(asyncio.wait(tasks))
    ioloop.close()

    conn.send(bytes("", encoding='UTF-8'))
conn.close()
def factorial(n):
    factorial = 1
    time.sleep(.5)
    if int(n) >= 1:
        for i in range(1, int(n)+1):
            factorial = factorial * i
    return factorial
with concurrent.futures.ProcessPoolExecutor() as executor:
    nums = range(50)
    results = executor.map(factorial, nums)
result = sum(results)
cur_time = time.time()

print(f"Final result = {result}")
print(f"Duration time: {time.time() - cur_time}")
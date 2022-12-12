# Yatluk Pavlo
# dz_12
# 1. Факторіал числа. Написати код з допомогою ThreadPoolExecutor та ProcessPoolExecutor.
# Додати у програму код, який порівнює швидкість обчислень і виводить на друк найоптимальніший метод.

# З допомогою ThreadPoolExecutor
import concurrent.futures
import time

def factorial(n):
    factorial = 1
    time.sleep(.5)
    if int(n) >= 1:
        for i in range(1, int(n)+1):
            factorial = factorial * i
    return factorial
with concurrent.futures.ThreadPoolExecutor() as executor:
    nums = range(50)
    results = executor.map(factorial, nums)
result = sum(results)
cur_time = time.time()

print(f"Final result = {result}")
print(f"Duration time: {time.time() - cur_time}")


# З допомогою ProcessPoolExecutor
import concurrent.futures
import time

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
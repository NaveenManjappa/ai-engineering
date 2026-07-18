import asyncio
import time

async def task_one():
    await asyncio.sleep(1)
    print("Task 1")


async def task_two():
    await asyncio.sleep(2)
    print("Task 2")


async def main():
    #Sequential
    start = time.perf_counter()
    await task_one()
    await task_two()
    end = time.perf_counter()
    print(f"Sequential Duration: {end-start:.2f} seconds")
    
    start = time.perf_counter()
    await asyncio.gather(task_one(), task_two())
    end = time.perf_counter()
    print(f"Concurrent Duration: {end-start:.2f} seconds")


asyncio.run(main())

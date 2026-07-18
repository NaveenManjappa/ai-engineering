import asyncio


async def faulty_task():
    await asyncio.sleep(3)
    raise ValueError("Something went wrong")


async def main():
    try:
        await faulty_task()
    except Exception as e:
        print(f"Exception occurred: {e}")


asyncio.run(main())

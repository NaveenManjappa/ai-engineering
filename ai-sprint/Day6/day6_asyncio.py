import asyncio


async def fetch_left():
    await asyncio.sleep(2)
    return "Left data"


async def fetch_right():
    await asyncio.sleep(2)
    return "Right data"


async def main():
    results = await asyncio.gather(fetch_left(), fetch_right())
    print(results)


asyncio.run(main())

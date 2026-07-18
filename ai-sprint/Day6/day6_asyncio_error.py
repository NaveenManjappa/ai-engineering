import asyncio


async def division(a, b):
    await asyncio.sleep(1)
    return a / b


async def main():
    results = await asyncio.gather(
        division(10, 2),
        division(12, 2),
        division(14, 0),
        division(16, 2),
        return_exceptions=True,
    )
    print(results)
    return results


print(asyncio.run(main()))

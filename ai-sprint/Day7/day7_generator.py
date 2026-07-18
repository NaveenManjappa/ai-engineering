import httpx
import asyncio


async def live_data_stream():
    for i in range(1, 4):
        await asyncio.sleep(1)
        yield f"Chunk: {i}"

async def main():
    async for chunk in live_data_stream():
        print(f"Received {chunk}")

asyncio.run(main())

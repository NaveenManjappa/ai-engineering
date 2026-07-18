import asyncio
import httpx

async def stream_large_file():
  async with httpx.AsyncClient() as client:
    async with client.stream("GET","https://jsonplaceholder.typicode.com/posts/1") as response:
      async for line in response.aiter_lines():
        if line:
          print(f"Streamed line {line}")

asyncio.run(stream_large_file())
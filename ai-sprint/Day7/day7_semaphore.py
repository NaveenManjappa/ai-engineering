import asyncio
import httpx

sem = asyncio.Semaphore(3)

async def fetch_with_limit(client,post_id):
  async with sem:
    print(f"Post {post_id} entered the semaphore slot")
    url=f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = await client.get(url,timeout=5)

    await asyncio.sleep(5)
    return response.json()
async def main():
  async with httpx.AsyncClient() as client:
    await asyncio.gather(*(fetch_with_limit(client,post_id) for post_id in range(1,11)))

asyncio.run(main())
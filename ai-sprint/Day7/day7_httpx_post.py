import httpx
import asyncio


async def send_prompt(client):
    url = "https://jsonplaceholder.typicode.com/posts"
    body = {
        "title": "Learning Async python",
        "body": "Concurrently mastering HTTP requests",
        "userId": 1,
    }
    headers = {"Authorization":"Bearer my_key"}
    response = await client.post(url, json=body,headers=headers)
    return response.json()


async def main():
    async with httpx.AsyncClient() as client:
        result = await send_prompt(client)
        print(result)


asyncio.run(main())

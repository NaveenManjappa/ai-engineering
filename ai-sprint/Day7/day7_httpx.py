import asyncio
import httpx
import time


async def fetch_post(client, post_id):
    if post_id == 5:
        raise RuntimeError("Simulated network error")
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = await client.get(url, timeout=5)
    return response.json()


async def main():
    async with httpx.AsyncClient() as client:
        # Sequential fetching
        start_seq = time.perf_counter()
        seq_results = []
        for post_id in range(1, 11):
            try:
                post = await fetch_post(client, post_id)
                seq_results.append(post)
            except Exception as e:
                seq_results.append(e)
        end_seq = time.perf_counter()
        # print(seq_results)
        print(f"Sequential took: {end_seq - start_seq:.2f} seconds")

        start_async = time.perf_counter()
        tasks = [fetch_post(client, post_id) for post_id in range(1, 11)]
        async_results = await asyncio.gather(*tasks, return_exceptions=True)
        end_async = time.perf_counter()
        # print(async_results)
        print(f"Concurrent took: {end_async - start_async:.2f} seconds")
        print(f"Result for Post 4: {type(async_results[3])}")
        print(f"Result for Post 5:{type(async_results[4])} -> {async_results[4]}")
        for result in async_results:
            if isinstance(result, Exception):
                print(f"Error happened while fetching this post, {result}")
            else:
                print(f"Title: {result.get('title')}")


asyncio.run(main())

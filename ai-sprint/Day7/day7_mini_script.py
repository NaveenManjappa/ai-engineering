import asyncio
import httpx
from unittest.mock import AsyncMock


async def fetch_prompt(client, prompt_id, semaphore, retries=2):
    async with semaphore:
        for attempt in range(retries + 1):
            try:
                print(f"Prompt id {prompt_id} Attempt={attempt + 1}/{retries + 1}...")
                response = await client.post(
                    "https://httpbin.org/post",
                    json={"prompt_id": prompt_id},
                    timeout=2.0,
                )
                response.raise_for_status()

                return response.json()
            except (httpx.HTTPStatusError, httpx.TimeoutException) as e:
                
                is_503 = (
                    isinstance(e, httpx.HTTPStatusError)
                    and e.response.status_code == 503
                )
                if (
                    isinstance(e, httpx.TimeoutException) or is_503
                ) and attempt < retries:
                    await asyncio.sleep(1)
                    continue
                else:
                    return f"Task {prompt_id} failed permanently: {e}"


async def main():
    prompt_ids = [101, 102, 103, 104, 105]
    semaphore = asyncio.Semaphore(2)

    # timeout = httpx.Timeout(10.0, connect=2.0)
    async with httpx.AsyncClient(timeout=10.0) as client:
        # mock_response = httpx.Response(
        #     status_code=200,
        #     json={"json": {"prompt_id": 101, "result": "Success"}},
        # )

        # client.post = AsyncMock(return_value=mock_response)
        tasks = [fetch_prompt(client, pid, semaphore) for pid in prompt_ids]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for pid, result in zip(prompt_ids, results):
            if isinstance(result, dict):
                print(f"ID {pid}: Success {result['data']}")
            else:
                print(f"ID {pid}: {result}")


asyncio.run(main())

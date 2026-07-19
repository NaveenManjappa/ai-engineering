import asyncio
import httpx

# Limit to 5 concurrent API requests
GATEKEEPER = asyncio.Semaphore(5)

async def stream_llm_prompt(client, prompt):
    # Acquire a slot from the semaphore
    async with GATEKEEPER:
        url = "https://api.example.com/v1/chat/completions"
        payload = {"model": "llm-core", "prompt": prompt, "stream": True}
        
        # Stream the POST response
        async with client.stream("POST", url, json=payload) as response:
            async for line in response.aiter_lines():
                if line:
                    # Process each token as it lands
                    print(f"Token received for '{prompt[:10]}...': {line}")

async def main():
    prompts = [f"Write a story about topic {i}" for i in range(100)]
    
    async with httpx.AsyncClient() as client:
        # Create tasks for all 100 prompts
        tasks = [stream_llm_prompt(client, p) for p in prompts]
        # Run them concurrently (the semaphore handles throttling)
        await asyncio.gather(*tasks)

# asyncio.run(main())
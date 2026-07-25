import tiktoken
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

MODEL_PRICING = {"gpt-5.4-nano": {"input": 0.2, "output": 1.25}}


def count_message_tokens(messages: list[dict], model: str) -> int:
    """Calculates the total prompt tokens using tiktoken"""
    try:
        encoding = tiktoken.get_encoding("cl100k_base")
    except ValueError:
        encoding = tiktoken.get_encoding("cl100k_base")

    num_tokens = 0
    for msg in messages:
        for key, value in msg.items():
            num_tokens += len(encoding.encode(value))

    return num_tokens


def calculate_cost(prompt_tokens: int, completion_tokens: int, model: str) -> float:
    rates = MODEL_PRICING[model]
    return (prompt_tokens / 1000000) * rates["input"] + (
        completion_tokens / 1000000
    ) * rates["output"]


def get_usage_value(usage, key: str):
    if hasattr(usage, key):
        return getattr(usage, key)
    if isinstance(usage, dict):
        return usage[key]
    raise TypeError(f"Unsupported usage object: {type(usage)}")


def run_comparision():
    model_name = "gpt-5.4-nano"
    messages = [
        {
            "role": "system",
            "content": "You are a concise AI assistant that provides brief answers.",
        },
        {
            "role": "user",
            "content": "Explain the difference between input and output tokens in 2 sentences.",
        },
    ]

    local_prompt_tokens = count_message_tokens(messages, model_name)

    print("Sending request to OpenAI")
    client = OpenAI()

    response = client.responses.create(model=model_name, input=messages)

    api_usage = response.usage

    try:
        encoding = tiktoken.get_encoding("cl100k_base")
    except ValueError:
        encoding = tiktoken.get_encoding("cl100k_base")

    local_completion_tokens = len(encoding.encode(response.output_text))

    estimated_cost = calculate_cost(
        local_prompt_tokens, local_completion_tokens, model_name
    )

    api_input_tokens = get_usage_value(api_usage, "input_tokens")
    api_output_tokens = get_usage_value(api_usage, "output_tokens")

    actual_cost = calculate_cost(api_input_tokens, api_output_tokens, model_name)

    print("\n" + "=" * 50)
    print("Assistane response:")
    print(response.output_text)
    print("=" * 50)
    print("\n Token Usage")
    print(f"{'Metric':<25} | {'tiktoken(local)':<18} | {'api_usage':<18}")
    print(
        f"{'Prompt Input tokens':<25} | {local_prompt_tokens:<18} | {api_input_tokens}"
    )
    print(
        f"{'Output tokens':<25} | {local_completion_tokens:<18} | {api_output_tokens}"
    )

    print("\n Cost Comparison")
    print(f"{'Estimated Cost':<25} | ${estimated_cost:<6f}")
    print(f"{'Actual Cost':<25} | ${actual_cost:<6f}")


if __name__ == "__main__":
    run_comparision()

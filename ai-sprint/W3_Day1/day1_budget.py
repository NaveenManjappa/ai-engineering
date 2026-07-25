def count_tokens(msgs):
    total_tokens = 0

    for msg in msgs:
        total_tokens += len(msg["content"].split(" "))
    return total_tokens


def trim_history(msgs, budget):
    msg_token = 0
    if msgs[0]["role"] == "system":
        msg_token = count_tokens([msgs[0]])
    start_idx = 0
    for i, msg in enumerate(msgs[::-1]):
        if msg["role"] == "system":
            continue
        msg_token += count_tokens([msg])
        if msg_token > budget:
            start_idx = len(msgs) - i
            break
    if start_idx < len(msgs) and msgs[start_idx]["role"] == "assistant":
        start_idx += 1
    trimmed = []
    if msgs[0]["role"] == "system":
        trimmed.append(msgs[0])
    trimmed.extend(msgs[start_idx:])
    return trimmed


# Generate 50 turns (101 messages total including system prompt)
test_msgs = [{"role": "system", "content": "You are a helpful assistant."}]

for i in range(1, 51):
    test_msgs.append({"role": "user", "content": f"User question {i}"})
    test_msgs.append({"role": "assistant", "content": f"Assistant response {i}"})

trimmed = trim_history(test_msgs, 100)
print("\n--- Test Results ---")
print(f"System prompt preserved: {trimmed[0] == test_msgs[0]}")
print(f"Tokens after trim: {count_tokens(trimmed)} (<= {100})")
print(f"Most recent question kept: {trimmed[-2]['content']}")
print(f"Most recent response kept: {trimmed[-1]['content']}")

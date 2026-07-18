from typing import TypedDict

def add_item(item: str, database: list[str] | None = None) -> list[str]:
    if database is None:
        database = []
    database.append(item)
    return database


print(add_item("apple"))
print(add_item("mango"))


def configure_plot(*, title: str, grid: bool = True) -> None:
    print(f"Plotting: {title} (Grid:{grid})")


configure_plot(title="My awesome graph")


def sum_numbers(*args: int) -> int:
    print(type(args))
    return sum(args)


print(sum_numbers(1, 2, 3))


def print_metadata(**kwargs: str) -> None:
    for k, v in kwargs.items():
        print(f"{k}:{v}")


user_info = {"name": "Alice", "role": "developer"}
print_metadata(**user_info)
print_metadata(a="a", b="2")


def set_profile(*, username: str, status: str) -> None:
    print(f"User {username} is now {status}")


user_data = {"username": "code123", "status": "active"}

set_profile(**user_data)

class SummaryStats(TypedDict):
    original_length:int
    max_limit:int

def summarize(text: str | None = None, max_words: int = 50) -> SummaryStats:
    summary_stats:SummaryStats={"original_length":0,"max_limit":max_words}
    if text is not None:
        words = text.split()
        summary_stats["original_length"]=len(words)
    return summary_stats

print(summarize("This is a short sentence"))
print(summarize())

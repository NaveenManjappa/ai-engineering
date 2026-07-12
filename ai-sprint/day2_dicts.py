# =============
# PART 1 DICTS
# =============
user = {"name": "Naveen", "role": "dev", "years": 14}

# Lookup
print(user["name"])
# print(user["salary"])
print(user.get("salary"))
print(user.get("salary", 0))

for key in user.keys():
    print(key)

for key in user:
    print(key)

for v in user.values():
    print(v)

for k, v in user.items():
    print(f"{k}:{v}")

print("name" in user)
print("name1" in user)
user["email"] = "n@example.com"
user["years"] = 15
del user["email"]
name = "name"
print(user[name])
print(user)

# ===============
# List comprehensions
# ==================
# A comprehension is a compact expression for creating a new list, dict, or set from an existing iterable.
# It is useful to revisit this syntax because it appears often in idiomatic Python.
nums = [1, 2, 3, 4, 5, 6, 7, 8]
squares = [n**2 for n in nums]
print(squares)

evens = [n for n in nums if n % 2 == 0]
print(evens)

even_squares = [n**2 for n in nums if n % 2 == 0]
print(even_squares)

users = [
    {"name": "Sam", "active": True},
    {"name": "Tom", "active": False},
    {"name": "Bob", "active": True},
]

print(users)

active_users = [u["name"] for u in users if u["active"]]
print(active_users)

# ============
# PART 3 DICT Comprehensions
# ============
square_map = {n: n * n for n in nums}
print(square_map)

active_lookup = {u["name"]: u["active"] for u in users if u["active"]}
print(active_lookup)

original = {"a": 1, "b": 2, "c": 3}
inverted = {original[k]: k for k in original}
print(inverted)
inverted = {v: k for k, v in original.items()}
print(inverted)

# ==============
# PART 4 Nested comprehensions
# ==============
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [num for row in matrix for num in row]
print(flat)

flat_manual = []
for row in matrix:
    for num in row:
        flat_manual.append(num)

print(flat == flat_manual)
print(flat is flat_manual)

flat_evens = [num for row in matrix for num in row if num % 2 == 0]
print(flat_evens)

colors = ["red", "blue", "green"]
size = ["S", "L"]
combos = [(c, s) for c in colors for s in size]
print(combos)

# =======
# DRILS
# ========
data = [[1, 2], [3, 4], [5, 6]]
words = ["hello", "hi", "hey", "yo"]
people = [
    {"name": "Naveen", "age": 39, "city": "Reading"},
    {"name": "Sam", "age": 25, "city": "London"},
    {"name": "Priya", "age": 31, "city": "Reading"},
]

# DRILL 1 — say what this produces:
d1 = [w.upper() for w in words if len(w) <= 2]


# DRILL 2 — dict comprehension:
d2 = {w: len(w) for w in words}


# DRILL 3 — filter on objects into a dict:
d3 = {p["name"]: p["city"] for p in people if p["city"] == "Reading"}


# DRILL 4 — NESTED. Narrate: "for each row, for each n in row, ..."
d4 = [n * 10 for row in data for n in row]


# DRILL 5 — NESTED + filter. This is the boss level. Read it aloud first.
d5 = [n for row in data for n in row if n % 2 == 1]


# Reveal by running:
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)

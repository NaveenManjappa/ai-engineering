# Two ways to reverse a string: using an iterator and using slicing.
# This is a good place to review how Python handles sequences and iteration.
def reverse_string(text):
    reversed_text = ""
    for t in reversed(text):
        reversed_text += t
    return reversed_text


def reverse_slice(text):
    return text[::-1]


print(reverse_string("Apple"))

print(reverse_slice("Apple"))

# FizzBuzz is a classic practice problem for loops and conditionals.
# Revisiting this later can help reinforce modulo (%) logic and order of if/elif branches.
def fizzbuzz():
    for i in range(1, 101, 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} FizzBuzz")
        elif i % 3 == 0:
            print(f"{i} Fizz")
        elif i % 5 == 0:
            print(f"{i} Buzz")
        else:
            print(i)


fizzbuzz()

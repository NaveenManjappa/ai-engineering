def chunk_generator(result):
    for i in range(4):
        yield f"{result}: {i + 1}"


generator_object = chunk_generator("Chunks")
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))

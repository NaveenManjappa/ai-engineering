import sys
input = {"a": 1, "b": 2, "c": 3.0}
input2 = {}


def double(number):
    return number * 2


def transform_dict(data, fn, transform_key=False):
    return {fn(k) if transform_key else k: fn(v) for k, v in data.items()}


print(transform_dict(input, double))
print(transform_dict(input, str))
print(transform_dict(input, lambda x: x**2))
print(transform_dict(input2, str))
print(transform_dict(input, double,True))


def transform_dict_except(data, fn, transform_key=False):
    result = {}
    for k, v in data.items():
        try:
            new_key = fn(k) if transform_key else k
            new_value = fn(v)
            result[new_key] = new_value
        except Exception as e:
            # print(e)
            continue
    return result


print(transform_dict_except(input, lambda x: x**2, False))
print(transform_dict_except(input, lambda x: x**2, True))

print(sys.path)

def second_index(text, some_str):
    first_index = text.find(some_str)
    if first_index == -1:
        return None

    second_index = text.find(some_str, first_index + 1)
    return second_index if second_index != -1 else None

assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", "h") is None
assert second_index("Hello, hello", "lo") == 10
print('ОК')
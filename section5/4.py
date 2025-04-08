def apply(lst, fn):
    result = []
    for elem in lst:
        result.append(fn(elem))
    return result

add_1 = lambda num : num + 1


r = apply([1, 2, 3], add_1)
print(r)
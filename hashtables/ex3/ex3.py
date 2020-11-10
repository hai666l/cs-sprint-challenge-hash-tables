def intersection(arrays):
    d = dict()
    r = []
    for arr in arrays:
        for n in arr:
            if n in d and n not in r:
                r.append(n)
            d[n] = None
    return r


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

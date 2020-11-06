def has_negatives(a):
    result = []
    d = dict()
    for n in a:
        n = abs(n)
        if n not in d:
            d[n] = None
        else:
            del d[n]
            result.append(n)
            
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

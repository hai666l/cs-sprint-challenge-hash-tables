def finder(files, queries):
    result = []
    for q in queries:
        for f in files:
            if len(q) <= len(f):
                if q == f[len(f)-len(q):]:
                    result.append(f)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

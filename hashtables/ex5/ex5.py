def finder(files, queries):
    d = dict()
    for f in files:
        for i in range(len(f)-1, 0, -1):
            if f[i] == '/':
                key = f[i+1:]
                if key not in d.keys():
                    d[key] = [f]
                else:
                    d[key].append(f)
                break
    r = []
    for q in queries:
        if q in d.keys():
            for s in d[q]:
                r.append(s)
    return r

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

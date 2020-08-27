import sys


def error(s):
    print(s, file=sys.stderr)
    sys.exit(1)


def readints():
    return map(int, input().split())


def readint():
    return int(input())


def readsplit():
    return input().split()


def readlistint():
    return list(readints())


def readsetint():
    return set(readints())


def readlist():
    return list(readsplit())


# input file
B, L, D = readints()
scores = readlistint()

libraries = []
for _ in range(L):
    Nj, Tj, Mj = readints()
    ids = readsetint()
    libraries.append((Nj, Tj, Mj, ids))

# output file
score = 0
books = set()
time = 0

A = readint()
if A < 0 or A > L:
    error("The number of libraries must be between 0 and {}".format(L))

for i in range(A):
    Y, K = readints()
    Nj, Tj, Mj, idset = libraries[Y]
    if Y < 0 or Y >= L:
        error(
            "Line {} ({}th library printed): the id must be between 0 and {}".
            format(2 * i + 2, i, L))
    if K < 1 or K > Nj:
        error(
            "Line {} ({}: {}th library printed): the number of books scanned from the library must positive and lower than the number of books in the library ({})"
            .format(2 * i + 2, Y, i, Nj))
    ids = readlistint()
    if len(ids) != K:
        error(
            "Line {} ({}: {}th library printed): there must be as many books as printed"
            .format(2 * i + 3, Y, i))
    if len(ids) != len(set(ids)):
        error(
            "Line {} ({}: {}th library printed): the ids of the books must be distincts"
            .format(2 * i + 3, Y, i))

    for e in ids:
        if not e in idset:
            error(
                "Line {} ({}: {}th library printed): all scanned books must be in the library"
                .format(2 * i + 3, Y, i))

    time += Tj
    n = min(K, (D - time) * Mj)
    for j in range(n):
        e = ids[j]
        if e not in books:
            books.add(e)
            score += scores[e]

for i in enumerate(sys.stdin):
    error("Too much lines")

print(score)

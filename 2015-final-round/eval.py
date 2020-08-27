import sys


def error(s):
    print(s, file=sys.stderr)
    sys.exit(1)


# input file
R, C, A = map(int, input().split())
L, V, B, T = map(int, input().split())
r0, c0 = map(int, input().split())

targets = set()
for _ in range(L):
    ri, ci = map(int, input().split())
    targets.add((ri, ci))

power = [[]]
for i in range(A):
    alt = []
    for j in range(R):
        row = []
        l = list(map(int, input().split()))
        for k in range(C):
            row.append((l[2 * k], l[2 * k + 1]))
        alt.append(row)
    power.append(alt)


# helper function
def inRange(pos1, pos2):
    return (pos1[0] - pos2[0])**2 + min(abs(pos1[1] - pos2[1]),
                                        C - abs(pos1[1] - pos2[1]))**2 <= V**2


# output file
alti = [0] * B
pos = [(r0, c0) for _ in range(B)]
valid = [True] * B
num = 0
score = 0
seen = set()

for num, line in enumerate(sys.stdin):
    num += 1
    if num > T:
        error("Too much lines")
    line = list(map(int, line.split()))
    if len(line) != B:
        error("Line {}: there must be {} numbers".format(num, B))
    seen.clear()

    for i, d in enumerate(line):
        if d not in {-1, 0, 1}:
            error("Line {}: all numbers must be either -1, 0 or 1".format(num))
        if alti[i] <= 1 and d == -1:
            error("Line {}: balloon {} cannot go down".format(num, i + 1))
        if alti[i] == A and d == 1:
            error("Line {}: balloon {} cannot go over {}".format(
                num, i + 1, A))

        alti[i] += d

        if not valid[i] or alti[i] == 0:
            continue

        row, col = pos[i]
        dr, dc = power[alti[i]][row][col]
        row += dr
        col += dc

        if row < 0 or row >= R:
            valid[i] = False
        if col < 0:
            col += C
        if col >= C:
            col -= C

        pos[i] = (row, col)

        if not valid[i]:
            continue

        for x in range(-V, V + 1):
            for y in range(-V, V + 1):
                t = (row + x, col + y)
                if t in targets and not t in seen and inRange(t, pos[i]):
                    seen.add(t)

    score += len(seen)

if num != T:
    error("There must be {} lines".format(T))

print(score)

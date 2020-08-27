import sys

R, C, F, N, B, T = map(int, input().split())

rides = []
for i in range(N):
    rides.append(list(map(int, input().split())))
    # a b x y s f

assigned = [None] * N

j = 0
score = 0
for j, line in enumerate(sys.stdin):
    j += 1
    if j > F:
        print("Too much lines were printed in the output file.")
        sys.exit(1)

    ride = list(map(int, line.split()))

    if not ride:
        print("Line {} is empty".format(j))
        sys.exit(1)

    if ride[0] > N:
        print("Line {}: The number of rides is superior to N".format(j))
        sys.exit(1)

    if ride[0] < 0:
        print("Line {}: The number of rides is negative".format(j))
        sys.exit(1)

    if len(ride) != 1 + ride[0]:
        print("Line {} is supposed to contain {} rides".format(j, 1 + ride[0]))
        sys.exit(1)

    posx, posy, time = 0, 0, 0
    for i in range(1, 1 + ride[0]):
        num = ride[i]
        a, b, x, y, s, f = rides[num]
        if num < 0 or num >= N:
            print("Line {}: {} is not a valid ride number".format(j, num))
            sys.exit(1)
        if assigned[num] is not None:
            print("Line {}: ride {} was already assigned to {}".format(
                j, num, assigned[num]))
            sys.exit(1)
        assigned[num] = j
        if time < s:
            time = s
        time += abs(posx - a) + abs(posy - b)
        if time == s:
            score += B
        time += abs(x - a) + abs(y - b)
        if time > T:
            break
        if time <= f:
            score += abs(x - a) + abs(y - b)
        posx = x
        posy = y

if j != F:
    print("{} lines were given while {} were expected".format(j, F))
    sys.exit(1)

print(score)

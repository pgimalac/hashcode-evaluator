import sys

N = int(input())
tags = []
used = []
orient = []
for i in range(N):
    line = input().split(" ")
    used.append(False)
    orient.append(line[0] == "H")
    line = line[2:]
    map(int, line)
    tags.append(set(line))

slides = int(input())
prev = set()
cur = set()
score = 0
for _ in range(slides):
    line = input().split(" ")
    if len(line) == 1:
        i = int(line[0])
        if not orient[i]:
            print("two photos needed if vertical")
            sys.exit(1)
        if used[i]:
            print("photo already used " + str(i))
            sys.exit(1)
        used[i] = True
        tag = tags[i]
    else:
        i = int(line[0])
        j = int(line[1])
        if orient[i] or orient[j]:
            print("to display 2 photos, they must be vertical")
            sys.exit(1)
        if used[i]:
            print("photo already used " + str(i))
            sys.exit(1)
        used[i] = True
        if used[j]:
            print("photo already used " + str(j))
            sys.exit(1)
        used[j] = True
        tag = tags[i] | tags[j]
    prev, cur = cur, tag
    score += min(len(prev & cur), min(len(prev - cur), len(cur - prev)))

print(score)

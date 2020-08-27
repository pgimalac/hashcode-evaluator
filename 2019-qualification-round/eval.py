import sys

# input file
N = int(input())
tags = []
used = []
orient = []
for i in range(N):
    line = input().split()
    used.append(False)
    orient.append(line[0] == "H")
    tags.append(set(line[2:]))

# output file and scoring
slides = int(input())
if slides <= 0 or slides > N:
    print("Invalid number of slides {}".format(slides))
    sys.exit(1)

prev = set()
cur = set()
score = 0
for line_num in range(2, 2 + slides):
    line = input().split()
    if len(line) == 1:
        i = int(line[0])
        if not orient[i]:
            print(
                "Line {}: two photos are needed for vertical pictures".format(
                    line_num))
            sys.exit(1)
        if used[i]:
            print("Line {}: photo {} has already been used".format(
                line_num, i))
            sys.exit(1)
        used[i] = True
        tag = tags[i]
    elif len(line) > 2:
        print("Line {}: too much arguments".format(line_num))
    else:
        i = int(line[0])
        j = int(line[1])
        if orient[i] or orient[j]:
            print("Line {}: both photos aren't vertical".format(line_num))
            sys.exit(1)
        if used[i]:
            print("Line {}: photo {} has already been used".format(
                line_num, i))
            sys.exit(1)
        used[i] = True
        if used[j]:
            print("Line {}: photo {} has already been used".format(
                line_num, j))
            sys.exit(1)
        used[j] = True
        tag = tags[i] | tags[j]
    prev, cur = cur, tag
    score += min(len(prev & cur), min(len(prev - cur), len(cur - prev)))

print(score)

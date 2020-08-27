import sys

# input files
V, E, R, C, X = map(int, input().split())
sizes = list(map(int, input().split()))

endpoints = []
for _ in range(E):
    latency, K = map(int, input().split())

    datas = {}
    for _ in range(K):
        c, lc = map(int, input().split())
        datas[c] = lc
    endpoints.append((latency, datas))

requests = []
for _ in range(R):
    rv, re, rn = map(int, input().split())
    requests.append((rv, re, rn))

# output file
N = int(input())
if N < 0 or N > C:
    print("Invalid number of cache server ({})".format(N))
    sys.exit(1)

servers = {}
for i in range(2, N + 2):
    line = list(map(int, input().split()))
    ident = line[0]
    if ident < 0 or ident >= C:
        print("Line {}: invalid id ({})".format(i, ident))
        sys.exit(1)
    if ident in servers:
        print("Server {} appears multiple times".format(ident))
        sys.exit(1)
    videos = line[1:]
    servers[ident] = set(videos)
    if len(servers[ident]) != len(videos):
        print("Line {}: a videos appears multiple times".format(i))
        sys.exit(1)
    weight = sum([sizes[v] for v in videos])
    if weight > X:
        print(
            "Line {}: the total size of the videos is over the capacity of the server"
            .format(i))

# scoring
score = 0
total_nb_request = 0
for (rv, re, rn) in requests:
    Ld = endpoints[re][0]
    L = [Ld]
    for id_serv, latency in endpoints[re][1].items():
        if id_serv in servers and rv in servers[id_serv]:
            L.append(latency)
    total_nb_request += rn
    score += (Ld - min(L)) * rn
print(int(score * 1000 / total_nb_request))

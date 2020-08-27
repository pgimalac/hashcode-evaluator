import sys

# entry file
R, S, U, P, M = map(int, input().split())

pool = [[None for _ in range(S)] for _ in range(R)]
for _ in range(U):
    r, s = map(int, input().split())
    pool[r][s] = -1

servers = []
for _ in range(M):
    z, c = map(int, input().split())
    servers.append((z, c))

# submit file
pool_cap = [0 for _ in range(P)]
row_serv = [[] for _ in range(R)]
numbers = [0 for _ in range(R)]
server_to_pool = [-1 for _ in range(M)]
for server, line in enumerate(sys.stdin):
    if server >= M:
        print("There are too much lines")
        sys.exit(1)

    if line[0] != 'x':
        r, s, p = map(int, line.split())
        if r < 0 or r >= R:
            print("Line {}: Invalid row".format(server + 1))
            sys.exit(1)
        if s < 0 or s >= S:
            print("Line {}: Invalid slot".format(server + 1))
            sys.exit(1)
        if p < 0 or p >= P:
            print("Line {}: Invalid pool".format(server + 1))
            sys.exit(1)
        if s + servers[server][0] > S:
            print("Line {}: the server extends beyond the size of the row".
                  format(server + 1))
            sys.exit(1)
        for i in range(s, s + servers[server][0]):
            if pool[r][i] == -1:
                print(
                    "Line {}: the server is positionned on an unavailable slot"
                    .format(server + 1))
                sys.exit(1)
            if pool[r][i] is not None:
                print("Line {}: the server is positionned on another server".
                      format(server + 1))
                sys.exit(1)
            pool[r][i] = server

        numbers[r] += servers[server][0]
        pool_cap[p] += servers[server][1]
        row_serv[r].append(server)
        server_to_pool[server] = p

gcs = [[] for _ in range(P)]
for i in range(P):
    for r in range(R):
        gcs[i].append(
            sum([
                servers[server][1] for server in row_serv[r]
                if server_to_pool[server] == i
            ]))

score = min([pool_cap[i] - max(gcs[i]) for i in range(P)])
print(score)

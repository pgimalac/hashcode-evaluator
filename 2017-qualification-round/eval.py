class Endpoint:
    def __init__(self, id, server_latency):
        self.id = id
        self.server_latency = server_latency
        self.cache_servers = list()

    def add_cache_server(self, id, latency):
        self.cache_servers.append((id, latency))

class Request:
    def __init__(self, video, endpoint, nb_request):
        self.video = video
        self.endpoint = endpoint
        self.nb_request = nb_request

class Server:
    def __init__(self, info):
        self.id = info[0]
        self.videos = info[1:]

    def add_video(self, id_vid):
        videos.append(id_vid)

def score(videos, endpoints, requests, servers):
    score = 0
    total_nb_request = 0
    for r in requests:
        Ld = endpoints[r.endpoint].server_latency
        L = [Ld]
        for id_serv, latency in endpoints[r.endpoint].cache_servers:
            if id_serv in servers and r.video in servers[id_serv].videos:
                L.append(latency)
        total_nb_request += r.nb_request
        score += (Ld - min(L))*r.nb_request
    print(int(score * 1000 / total_nb_request))

if __name__ == "__main__":
    V, E, R, C, X = map(int, input().split())

    videos = list(map(int, input().split()))

    endpoints = {}
    for i in range(E):
        latency, K = map(int, input().split())
        endpoint = Endpoint(i, latency)
        for j in range(K):
            ident, serverlatency = map(int, input().split())
            endpoint.add_cache_server(ident, serverlatency)
        endpoints[i] = endpoint

    requests = list()
    for i in range(R):
        id_vid, id_end, nb_request = map(int, input().split())
        requests.append(Request(id_vid, id_end, nb_request))

    # début de la lecture de la solution
    
    S = int(input())
    servers = {}
    for i in range(S):
        info = list(map(int, input().split()))
        servers[info[0]] = Server(info)

    score(videos, endpoints, requests, servers)

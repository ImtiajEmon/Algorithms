from queue import Queue

def bfs(source):
    visited[source] = 1
    q = Queue()
    q.put(source)

    while not q.empty():
        frnt = q.get()

        for neighbour in adj_list[frnt]:
            if not visited[neighbour]:
                print(f"Going from {frnt} to {neighbour}")
                q.put(neighbour)
                visited[neighbour] = 1


#====================== Graph Building ==========================
nodes = int(input())
edges = int(input())

adj_list = [[] for i in range(nodes + 1)]
visited = [0] * int(nodes + 1)

# Taking the edges
for i in range(edges):
    u, v = map(int, input().split(' '))

    # For undirected graph
    adj_list[u].append(v)
    adj_list[v].append(u)
#=================================================================

bfs(1)

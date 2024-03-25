from queue import Queue

def bfs(source, col):
    color[source] = col
    q = Queue()
    q.put(source)

    while not q.empty():
        frnt = q.get()
        col = color[frnt]

        for neighbour in adj_list[frnt]:
            if color[neighbour] == 0:
                q.put(neighbour)
                color[neighbour] = col * -1

            elif color[neighbour] == col:
                return False

    return True


#====================== Graph Building ==========================
nodes = int(input())
edges = int(input())

adj_list = [[] for i in range(nodes + 1)]

# Taking the edges
for i in range(edges):
    u, v = map(int, input().split(' '))

    # For undirected graph
    adj_list[u].append(v)
    adj_list[v].append(u)
#=================================================================
color = [0] * int(nodes + 1)

if bfs(1, 1):
    print("Bipartite")
else:
    print("Not Bipartite")

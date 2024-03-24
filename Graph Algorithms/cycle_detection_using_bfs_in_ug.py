from queue import Queue

def checkCycle(source, parent):
    visited[source] = 1
    q = Queue()
    q.put((source, parent))

    while not q.empty():
        frnt = q.get()
        u = frnt[0]
        parent = frnt[1]

        for v in adj_list[u]:
            if visited[v] and v != parent:
                return True

            if not visited[v]:
                q.put((v, u))
                visited[v] = 1

    return False


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

if checkCycle(1, -1):
    print("There is a cycle")
else:
    print("No cycle")

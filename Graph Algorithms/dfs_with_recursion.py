def dfs(u):
    visited[u] = 1

    for v in adj_list[u]:
        if not visited[v]:
            #print(f"Going from {u} to {v}")
            dfs(v)

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

visited = [0] * (nodes + 1)
source = 1
dfs(source)

def dfs(u, col):
    color[u] = col

    for v in adj_list[u]:
        if color[v] == 0:
            if not dfs(v, col * -1):
                return False
        
        elif color[v]  == col:
            return False

    return  True

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

color = [0] * (nodes + 1)  # color = 0 => unvisited; color = 1 => visited & let say blue; color = -1 => visited & let say red
source = 1

if dfs(source, 1):
    print("Bipartite")
else:
    print("Not Bipartite")

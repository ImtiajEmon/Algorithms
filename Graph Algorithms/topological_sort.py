# Only   valid  on DAG
# linear ordering of vertices such that if there is a edge between u & v, then u appears before v

def dfs(u):
    visited[u] = 1

    for v in adj_list[u]:
        if not visited[v]:
            #print(f"Going from {u} to {v}")
            dfs(v)

    # store the node, when going backtracked from it
    # increasing order of node finishingtime
    top_order.append(u)   

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

visited = [0] * (nodes + 1)
top_order = []

source = 1
dfs(source)

# We need decreasing order of node finishing time
top_order.reverse()

print(top_order)

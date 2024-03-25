def dfs(u):
    stack.append(u)

    while len(stack) != 0:
        top = stack.pop()
        visited[top] = 1

        for v in adj_list[top]:
            if not visited[v]:
                print(f"Going from{top} to {v}")
                stack.append(v)

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
stack = []
source = 1

dfs(source)

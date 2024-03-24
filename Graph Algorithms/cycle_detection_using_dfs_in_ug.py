def check_cycle(u, parent):
    visited[u] = 1

    for v in adj_list[u]:
        if not visited[v]:
            if check_cycle(v, u):  # Here we only return true when it get true Bcz, if we return false also then it terminate the loop and return false.
                return True        # But there can be cycle in another branch

        elif v != parent:
            return True

    return False



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

visited = [0] * int(nodes + 1)

flag = False
for u in range(1, nodes+1):
    if visited[u]:
        continue

    flag = check_cycle(u, -1)
    if flag:
        break


if flag:
    print("The graph has a cycle")
else:
    print("The graph has no cycle")

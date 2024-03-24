def check_cycle(u):
    visited[u] = 1

    for v in adj_list[u]:
        if not visited[v]:
            if check_cycle(v):
                return True

        elif visited[v] == 1:
            return True

    visited[u] = 2
    return False



#====================== Graph Building ==========================
nodes = int(input())
edges = int(input())

adj_list = [[] for i in range(nodes + 1)]

# Taking the edges
for i in range(edges):
    u, v = map(int, input().split(' '))

    # For directed graph
    adj_list[u].append(v)
#=================================================================

visited = [0] * int(nodes + 1)

flag = False
for u in range(1, nodes+1):
    if visited[u]:
        continue

    flag = check_cycle(u)
    if flag:
        break


if flag:
    print("The graph has a cycle")
else:
    print("The graph has no cycle")

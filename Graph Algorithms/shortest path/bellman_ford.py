def bellmanFord(source, n):
    distance[source] = 0

    for i in range(n-1):
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w


    # nth relaxation to check negetive cycle
    # for u, v, w in edges:
    #     if distance[u] + w < distance[v]:
    #         return -1

#======================================================
node, edge = map(int, input().split())

edges = []
for i in range(edge):
    u, v, w = map(int, input().split())

    # For undirected graph
    edges.append((u, v, w))
    edges.append((v, u, w))

distance = [1e9] * (node+1)

bellmanFord(1, node)

for v in range(1, nodes+1):
    print("Distance from 1"," to ", v, "= ", distance[v])

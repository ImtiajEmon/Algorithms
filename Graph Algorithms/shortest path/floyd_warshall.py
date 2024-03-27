def floydWarshall(node):
    for k in range(1, node+1):
        for u in range(1, node+1):
            for v in range(1, node+1):
                if distance[u][k] + distance[k][v] < distance[u][v]:
                    distance[u][v] = distance[u][k] + distance[k][v]
                    #link[u][v] = link[u][k]

#===========================================================
node, edge =  map(int, input().split())

distance = [[0 if i == j else 1e18 for j in range(node+1)] for i in range(node+1)]

# To keep track of parent
#link = [[0 for j in range(node+1)] for i in range(node+1)]  



for i in range(edge):
    u, v, w = map(int, input().split())

    # for directed graph
    # We take min. bcz, there can be parallal edge. In case of that we take the edge with min weight
    distance[u][v] = min(distance[u][v], w)
    distance[v][u] = min(distance[v][u], w)

    #link[u][v] = v

floydWarshall(node)


# start, end = 1, node
# path = [start]

# while start != end:
#     start = link[start][end]
#     path.append(start)
# print(path)


for u in range(1, node+1):
    for v in range(1, node+1):
        print(distance[u][v], end = " ")
    print()

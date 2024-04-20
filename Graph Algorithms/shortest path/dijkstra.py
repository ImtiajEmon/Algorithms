from queue import PriorityQueue


def dijkstra(source):
    distance[source] = 0   # make source distance 0

    pq = PriorityQueue()

    pq.put((0, source))  #(cost, node)

    while not pq.empty():
        cost, u = pq.get()

        if distance[u] != cost:
            continue

        for new_cost, v in adj_list[u]:
            if cost + new_cost < distance[v]:
                distance[v] = cost + new_cost
                pq.put((distance[v], v))


#====================== Graph Building ==========================
nodes = int(input())
edges = int(input())

adj_list = [[] for i in range(nodes + 1)]

# Taking the edges
for i in range(edges):
    u, v, cost = map(int, input().split(' '))

    # For undirected graph
    adj_list[u].append((cost, v))
    adj_list[v].append((cost, u))
#=================================================================

distance = [1e9] * (nodes+1)  # make all distance to infinity

dijkstra(1)

for v in range(1, nodes+1):
    print("Distance from 1"," to ", v, "= ", distance[v])

# Only   valid  on DAG
# linear ordering of vertices such that if there is a edge between u & v, then u appears before v
# Kahn's algorithm gives the verteces alphabetic order

from queue import PriorityQueue

def kahn():
    q = PriorityQueue() # to maintain alphabetical order
    
    for i in range(1, len(incoming_edge_count)):
        if incoming_edge_count[i] == 0:
            q.put(i)

    while not q.empty():
        frnt = q.get()
        top_order.append(frnt)

        for neighbour in adj_list[frnt]:
            incoming_edge_count[neighbour] -= 1

            if incoming_edge_count[neighbour] == 0:
                q.put(neighbour)

#====================== Graph Building ==========================
nodes = int(input())
edges = int(input())

adj_list = [[] for i in range(nodes + 1)]
incoming_edge_count = [0] * int(nodes + 1)

# Taking the edges
for i in range(edges):
    u, v = map(int, input().split(' '))

    # For undirected graph
    adj_list[u].append(v)
    adj_list[v].append(u)
    incoming_edge_count[v] += 1
#=================================================================
top_order = []

kahn()

print(top_order)

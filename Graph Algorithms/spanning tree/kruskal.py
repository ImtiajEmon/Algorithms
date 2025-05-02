def makeset(u):
    master[u] = u
    size[u] = 1

def find(u):
    if master[u] == u:
        return u
    master[u] = find(master[u])
    return master[u]

def unite(u, v):
    if size[u] < size[v]:
        master[u] = v
        size[v] += size[u]
    else:
        master[v] = u
        size[u] += size[v]

#=========================================
nodes, edges = map(int, input().split())

master = [0] * (nodes+1)
size = [0] * (nodes+1)
edge_vertices = []

#making everyone's master itself and size 1
for i in range(1, nodes+1):
    makeset(i)

pair = [] # [(cost, index)] pair

for i in range(edges):
    u, v, c = map(int, input().split(' '))
    edge_vertices.append((u, v))
    pair.append((c, i))

pair.sort()


mst_cost = 0
edge_cnt = 0

for E in pair:
    u = edge_vertices[E[1]][0]
    v = edge_vertices[E[1]][1]

    u = find(u)
    v = find(v)
    if u == v:
        continue

    unite(u, v)
    mst_cost += E[0]
   


print(mst_cost)

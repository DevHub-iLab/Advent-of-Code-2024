import aocd
input = aocd.get_data(day=23, year=2024)

# input = """kh-tc
# qp-kh
# de-cg
# ka-co
# yn-aq
# qp-ub
# cg-tb
# vc-aq
# tb-ka
# wh-tc
# yn-cg
# kh-ub
# ta-co
# de-co
# tc-td
# tb-wq
# wh-td
# ta-ka
# td-qp
# aq-cg
# wq-ub
# ub-vc
# de-ta
# wq-aq
# wq-vc
# wh-yn
# ka-de
# kh-ta
# co-tc
# wh-qp
# tb-vc
# td-yn"""

input = [(x[0:2], x[3:5]) for x in input.split("\n")]

### Part 1 - Brute force enumeration of K_3 subgraphs
def adj_list(input):
    adj = {}
    for x in input:
        if x[0] not in adj:
            adj[x[0]] = []
        if x[1] not in adj:
            adj[x[1]] = []
        adj[x[0]].append(x[1])
        adj[x[1]].append(x[0])
    return adj

adj = adj_list(input)

# triplet of nodes that are connected to each other
def get_triplets(adj):
    triplets =  set()
    for x in adj:
        for y in adj[x]:
            for z in adj[y]:
                if z in adj[x]:
                    triplets.add(tuple(sorted([x, y, z])))

    return triplets

triplets = get_triplets(adj)

def has_t(triplet):
    for x in triplet:
        if x.startswith("t"):
            return True
    return False
# print(len(triplets))
count = 0
for x in triplets:
    count += has_t(x)
print(count)

### Part 2 - Find the unique maximal clique

# bron kerbosch algorithm for maximal cliques
def bron_kerbosch(adj, R, P, X, clique):
    if len(P) == 0 and len(X) == 0:
        clique.append(R)
        return
    for v in P.copy():
        bron_kerbosch(adj, R + [v], P.intersection(adj[v]), X.intersection(adj[v]), clique)
        P.remove(v)
        X.add(v)

cliques = []
bron_kerbosch(adj, [], set(adj.keys()), set(), cliques)
max_clique = max(cliques, key=len)
print(",".join(sorted(max_clique)))
import re
import networkx as nx
f = open("/workspaces/Advent-of-Code-2024/emily7lim/day23/data.txt", "r")
contents = f.read().split("\n")
glist = []
tlist = []
for i in contents:
    glist.append(sorted(i.split("-")))
    tlist.append(tuple(i.split("-")))

# part1
dictlist = {}
for key,value in sorted(glist):
    if key not in dictlist.keys():
        dictlist[key] = [value]
    else:
        dictlist[key].append(value)

resultlist = []
for i in dictlist:
    for j in dictlist[i]:
        if j in dictlist.keys():
            for k in dictlist[j]:
                result = ""
                if k in dictlist[i]:
                    result = i+","+j+","+k
                    resultlist.append(result)

count = 0
for i in resultlist:
    if re.search(r"\b(t\w*)\b",i) != None:
        count += 1
print(count)

# part2
gra = nx.Graph()
gra.add_edges_from(tlist)
cliques = nx.find_cliques(gra)
largest_clique = max(cliques, key=len)
p2 = ""
for i in sorted(largest_clique):
    p2 = p2 + i + ","
print(p2[:-1])

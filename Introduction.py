from matplotlib import pyplot as plt
nodes = [ 
    { "id" : 0, "name": "brown node"},
    { "id" : 1, "name": "blue node"},
    { "id" : 2, "name": "yellow node"},
    { "id" : 3, "name": "purple node"},
    { "id" : 4, "name": "red node"},
    { "id" : 5, "name": "white node"},
    { "id" : 6, "name": "green node"},
    { "id" : 7, "name": "orange node"},
    { "id" : 8, "name": "black node"},
    { "id" : 9, "name": "gray node"},
]

junctions = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9), (9,0)]

# create an empty list for each node
for node in nodes:
    node["junctions"] = []

# populate the lists with the junctions
for i, j in junctions:
    nodes[i]["junctions"].append(nodes[j])
    nodes[j]["junctions"].append(nodes[i])

def number_of_junctions(node):
    return len(node["junctions"])

total_junctions = sum(number_of_junctions(node) for node in nodes)

num_junctions = len(nodes)
avg_junctions = total_junctions / num_junctions
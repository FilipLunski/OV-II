from itertools import combinations

max_distance = 15

# matrix representing distances between cities
distance_matrix = [
    [0, 10, 20, 30, 30, 20],
    [10, 0, 25, 35, 20, 10],
    [20, 25, 0, 15, 30, 20],
    [30, 35, 15, 0, 15, 25],
    [30, 20, 30, 15, 0, 14],
    [20, 10, 20, 25, 14, 0] 
]

# alternative matrix for prooving program works when there is multiple optimal solutions and it finnds them all
# distance_matrix = [
#     [0, 10, 20, 20, 30, 20],
#     [10, 0, 15, 25, 20, 10],
#     [20, 15, 0, 15, 15, 20],
#     [20, 25, 15, 0, 20, 25],
#     [30, 20, 15, 15, 0, 15],
#     [20, 10, 20, 25, 15, 0] 
# ]

# list of cities
nodes = list(range(1,len(distance_matrix)+1))

# function to create adjacency list by given distance matrix and max distance
def create_adjacency_list(distance_matrix, max_distance):
    adjacency_list = {}
    for i, row in enumerate(distance_matrix):
        adjacency_list[i+1] = []
        for j, distance in enumerate(row):
            if distance <= max_distance:
                adjacency_list[i+1].append(j+1)
    return adjacency_list

# function to check if given nodes form a valid cover
def check_valid_cover(selected_nodes, adjacency_list):
    all_nodes = set()
    for node in selected_nodes:
        all_nodes.update(adjacency_list[node])
    return len(all_nodes) == len(adjacency_list)

# function to find minimal cover
def find_min_cover(distance_matrix, max_distance):

    adjacency_list = create_adjacency_list(distance_matrix, max_distance)


    minimal_cover = []
    minimal_size = float("inf")

    # iterate over all lengths of combinations of nodes
    for i in range(1, len(nodes)+1):
        # iterate over all combinations of nodes of given length
        for combination in combinations(nodes, i):
            # if combination is valid cover, save it
            if check_valid_cover(combination, adjacency_list):
                minimal_size = i
                minimal_cover += [combination]
        # if minimal cover is found, return it as next iteration will only find covers of greater size
        if minimal_size != float("inf"):
            return minimal_cover, minimal_size
    
print(find_min_cover(distance_matrix, max_distance))
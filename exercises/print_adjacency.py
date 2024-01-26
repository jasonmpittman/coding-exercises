__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Print Adjacency: https://www.geeksforgeeks.org/print-adjacency-list-for-a-directed-graph/

Given the adjacency list and number of vertices and edges of a graph, the task is to represent the adjacency list for a directed graph.

Example:
    Input: V = 3, edges[][]= {{0, 1}, {1, 2} {2, 0}}
    Output:     0 -> 1
                1 -> 2
                2 -> 0

Started: Jan 26, 2024 @ 4:15am ET
Intervals: 1
Ended: Jan 26, 2024 @ 4:40am ET                
"""

# TODO: done but small bug with the 1,2 1,3
def find_adjacencies(vertices: int, edges: list):
    for adjacency in edges:
        x = adjacency[0]
        y = ""

        for edge in edges:
            if x == edge[0]:
                y += " " + str(edge[1])
        
        print(x, " -> ", y)
        

if __name__ == '__main__':
    vertices = 3
    edges = [[0,1], [1,2], [2,0]]
    #edges = [[0, 1], [1, 2], [1, 3], [2, 3], [3, 0]]

    find_adjacencies(vertices, edges)
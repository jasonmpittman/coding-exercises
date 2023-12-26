__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" BFS Unweighted

Write a function that finds the shortest path between two nodes in an unweighted graph. The graph will be represented as an adjacency list, and you need to implement a Breadth-First Search (BFS) algorithm to find the shortest path.

Given an unweighted graph represented as an adjacency list and two nodes (start and end), find the shortest path from the start node to the end node. If no path exists, your function should indicate that as well.

The function should return the shortest path as a list of nodes from the start node to the end node, inclusive. For example, find_shortest_path(graph, 'A', 'F') should return ['A', 'C', 'F'].

If there is no path from the start node to the end node, the function can return None or an appropriate message.

Started: Dec 17, 2023 @ 9:45am ET
Intervals: 1
Ended: Dec 17, 2023 @ 10:15am ET  
"""

def find_shortest_path(graph, start, end):
    visited = {} 
    queue = []
    found = True
    current_node = ''

    while found:

        if len(queue) != 0:
            # take current node in queue
            current_node = queue.pop(-1)

            # get neighbors from graph and add to queue

            # if current_node is target, 
            if current_node == end:
                found = False
                break
        else:
            queue.append(start)
            print(queue)
    

        

if __name__ == '__main__':
    graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

    find_shortest_path(graph, 'A', 'F')
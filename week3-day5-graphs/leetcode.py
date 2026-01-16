# In the session we covered LeetCode Problem 1971: Find if path exists in Graph
# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = { i: [] for i in range(n) }

        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([source])
        visited = set([source])

        # Breadth First Search
        while queue:
            vertex = queue.popleft()

            # Perform any operation with the vertex
            if vertex == destination:
                return True

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return False
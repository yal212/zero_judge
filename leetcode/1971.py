from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        if not edges:
            return False
        paths = defaultdict(list)
        for a, b in edges:
            paths[a].append(b)
            paths[b].append(a)
        queue = [source]
        visited = {source}
        while queue:
            cur = queue.pop()
            for path in paths[cur]:
                if path == destination:
                    return True
                if path not in visited:
                    queue.append(path)
                    visited.add(path)
        return False

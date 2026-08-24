class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        visit = set()
        queue = deque()

        queue.append((0, 0))
        visit.add((0, 0))

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        length = 1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == rows - 1 and c == cols - 1:
                    return length

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        (nr, nc) in visit or
                        grid[nr][nc] == 1
                    ):
                        continue

                    queue.append((nr, nc))
                    visit.add((nr, nc))

            length += 1

        return -1
    

1class Solution:
2    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
3        x_coords = []
4        y_coords = []
5        for rectangle in rectangles:
6            x_start, y_start, x_end, y_end = rectangle
7            x_coords.append((x_start, x_end))
8            y_coords.append((y_start, y_end))
9        x_coords.sort(key=lambda x: (x[1], x[0]))
10        y_coords.sort(key=lambda x: (x[1], x[0]))
1112        def countSegments(coords: list[tuple[int, int]]) -> int:
13            res = [coords[0]]
14            for coord in coords[1:]:
15                while res and res[-1][1] > coord[0]:
16                    coord = (
17                        min(res[-1][0], coord[0]),
18                        max(res[-1][1], coord[1])
19                    )
20                    res.pop()
21                res.append(coord)
22            return len(res)
232425        if countSegments(x_coords) >= 3 or countSegments(y_coords) >= 3:
26            return True
27        return False
28
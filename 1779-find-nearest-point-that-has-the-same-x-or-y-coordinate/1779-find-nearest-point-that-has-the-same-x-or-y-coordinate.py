class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        least = 10000000
        ind = 0
        cnt = 0
        for i in points:
            if (x == i[0]) or (y == i[1]):
                dist = abs(x-i[0]) + abs(y-i[1])
                if dist < least:
                    least = dist
                    ind = cnt
            cnt += 1
        if least == 10000000:
            return -1
        return ind
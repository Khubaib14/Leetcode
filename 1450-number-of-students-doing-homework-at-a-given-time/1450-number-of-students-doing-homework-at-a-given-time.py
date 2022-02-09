class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum([1 for start,end in zip(startTime, endTime) if queryTime in range(start, end+1) ])
        
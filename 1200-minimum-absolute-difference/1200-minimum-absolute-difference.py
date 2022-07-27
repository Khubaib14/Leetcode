class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        currdiff = 9999999
        result = []
        for i in range(1,len(arr)):
            diff = abs(arr[i-1] - arr[i])
            if diff < currdiff:
                currdiff = diff
                result = []
                temp = [arr[i-1],arr[i]]
                result.append(temp)
            elif diff == currdiff:
                temp = [arr[i-1],arr[i]]
                result.append(temp)
        return result
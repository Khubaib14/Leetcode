class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        slow = 0
        fast = 0
        total = 0
        count = 0

        while fast < len(arr):
            total += arr[fast]
            if fast - slow + 1 < k:
                fast += 1
            elif fast - slow + 1 == k:
                if total // k >= threshold:
                    count += 1
                total = total - arr[slow]
                fast += 1
                slow += 1

        return count
        
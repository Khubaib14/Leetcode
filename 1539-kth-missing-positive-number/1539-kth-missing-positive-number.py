class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        temp = [i for i in range(1, arr[-1] + k+1)]

        arrpoint = 0
        temppoint = 0
        cnt = 0

        while cnt < k:
            if arrpoint > len(arr) - 1:
                temppoint += (k - cnt)
                break

            if arr[arrpoint] == temp[temppoint]:
                arrpoint += 1
                temppoint += 1
            elif arr[arrpoint] != temp[temppoint]:
                temppoint += 1
                cnt += 1
        
        return temppoint
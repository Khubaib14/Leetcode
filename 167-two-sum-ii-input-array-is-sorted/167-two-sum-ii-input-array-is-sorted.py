class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1    
        q = []
        while l < r:
            if numbers[l] + numbers[r] == target:
                q.append(l+1)
                q.append(r+1)
                return q
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
        return q
        
        
        
        
        
        
    def Onsquare(self,numbers, target):  
        for i in range(len(numbers)):
            l = []
            to_find = target - numbers[i]
            print(to_find)
            for j in range(i+1, len(numbers)):
                if numbers[j] == to_find:
                    l.append(i+1)
                    l.append(j+1)
                    return l
        
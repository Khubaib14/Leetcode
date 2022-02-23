class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        point = 0
        num = 1
        q = []
        while num <= target[-1] or point < len(target):
            if num == target[point]:
                q.append("Push")
                point += 1
                num += 1
            elif num != target[point]:
                q.append("Push")
                q.append("Pop")
                num += 1    
        return q
        
        
    def solution_one(self, target: List[int], n: int):
        l = []
        for i in range(1,target[-1]+1):
            if i in target:
                l.append('Push')
            elif i not in target:
                l.append('Push')
                l.append('Pop')

        return l

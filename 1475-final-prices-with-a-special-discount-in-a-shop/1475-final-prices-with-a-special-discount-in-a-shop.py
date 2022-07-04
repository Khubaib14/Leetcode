class Solution:
    def NearestSmallertoRight(self, arr):
        result = []
        stk = []
        for i in range(len(arr)-1, -1, -1):
            if not stk:
                result.append(0)
            elif stk[-1] <= arr[i]:
                result.append(stk[-1])
            elif stk[-1] > arr[i]:
                while stk and stk[-1] > arr[i]:
                    stk.pop()
                if not stk:
                    result.append(0)
                else:
                    result.append(stk[-1])
            stk.append(arr[i])
        result.reverse()
        return result
    
    def finalPrices(self, prices: List[int]) -> List[int]:
        discount = self.NearestSmallertoRight(prices)
        return [(prices[i] - discount[i]) for i in range(len(prices))]
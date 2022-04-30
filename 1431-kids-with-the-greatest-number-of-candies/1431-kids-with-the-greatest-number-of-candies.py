class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxtemp = 0
        temp = 0
        result = []

        for i in candies:
            if i > maxtemp:
                maxtemp = i

        barrier = maxtemp - extraCandies
        
        for i in candies:
            if i>= barrier:
                result.append(True)
            else:
                result.append(False)

        return result   
        
        
    def Sol1(self, candies: List[int], extraCandies: int) -> List[bool]:       
        maxtemp = 0
        temp = 0
        result = []

        for i in candies:
            if i > maxtemp:
                maxtemp = i

        for i in candies:
            if (i + extraCandies) >= maxtemp:
                result.append(True)
            else:
                result.append(False)

        return result
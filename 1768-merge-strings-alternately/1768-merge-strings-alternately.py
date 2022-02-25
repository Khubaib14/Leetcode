class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r = ""

        for i in range(min(len(word1), len(word2))):
            r = r + word1[i] + word2[i]

        r = r + word1[i+1:] + word2[i+1:]
        
        return r
        
        
        
        
    def firstOne(word1: str, word2: str):
        s = ""
 
        point1 = 0
        point2 = 0

        while point1 < len(word1) or point2 < len(word2):
            if point1 == len(word1):
                s = s + word2[point2:]
                break
            elif point2 == len(word2):
                s = s + word1[point1:]
                break
            else:
                s = s + word1[point1]
                s = s + word2[point2]
                point1 += 1
                point2 += 1

        return s
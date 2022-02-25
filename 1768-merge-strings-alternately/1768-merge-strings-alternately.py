class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
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
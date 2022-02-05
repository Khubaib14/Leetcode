class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l = list(map(ord, list(sentence)))
        for i in range(97, 123):
            if i in l:
                pass
            else:
                return False
        return True
        
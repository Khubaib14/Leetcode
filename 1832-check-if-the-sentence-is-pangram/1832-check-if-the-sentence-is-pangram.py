class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l = [ord(i) for i in set(sentence)]
        # l = set(map(ord, set(sentence)))
        for i in range(97, 123):
            if i in l:
                pass
            else:
                return False
        return True
        
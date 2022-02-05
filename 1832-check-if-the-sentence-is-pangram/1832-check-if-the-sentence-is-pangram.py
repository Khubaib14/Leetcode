class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = [0] * 26
        l = [ord(i) for i in set(sentence)]
        for i in range(97, 123):
            if i in l and alphabets[i-97] == 0:
                alphabets[i-97] += 1
        print(alphabets)
        if sum(alphabets) == 26:
            return True
        return False
        
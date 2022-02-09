class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def gen(words):
            for word in words:
                for letter in word:
                    yield letter
            yield None
                    
        def check(word1, word2):
            for letter1, letter2 in zip(gen(word1), gen(word2)):
                if letter1 != letter2:
                    return False
            return True
        
        return check(word1, word2)
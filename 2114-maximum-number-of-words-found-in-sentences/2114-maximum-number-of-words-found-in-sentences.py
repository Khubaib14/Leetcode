class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum = 0
        for i in sentences:
            l = len(list(i.split(" ")))
            if l > maximum:
                maximum = l
        return maximum
class Solution:
    def DictMap(self, order):
        d = {}
        for i in range(len(order)):
            d[order[i]] = d.get(i, 0) + i
        return d

    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictmap = self.DictMap(order)
        for i in range(1, len(words)):
            a = words[i-1]
            b = words[i]
            for j in range(len(a)):
                if j == len(b):
                    return False
                char_a = a[j]
                char_b = b[j]
                if dictmap[char_a] < dictmap[char_b]:
                    break
                if dictmap[char_a] > dictmap[char_b]:
                    return False
        return True
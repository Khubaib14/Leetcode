class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}

        # making the hashmap
        for i in magazine:
            hashmap[i] = hashmap.get(i, 0) + 1

        # checking letters of ransomNote from hashmap
        for j in ransomNote:
            if j in hashmap and hashmap[j] > 0:
                hashmap[j] -= 1
            else:
                return False
        
        return True


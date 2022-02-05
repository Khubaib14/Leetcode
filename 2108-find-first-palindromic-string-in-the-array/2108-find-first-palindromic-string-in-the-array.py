class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def reverse_list(x):
            if len(x) < 2:
                return x
            else:
                return reverse_list(x[len(x)//2:]) + reverse_list(x[:len(x)//2])
        
        for i in words:
            t = i
            t = reverse_list(i)
            if t == i:
                return t
                break
        return "" 
        
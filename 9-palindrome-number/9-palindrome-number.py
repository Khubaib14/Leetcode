class Solution:
    def isPalindrome(self, n: int) -> bool:
        x = []
        
        def add_to_list(n: int):
            while n > 0:
                x.append(n%10)
                n = n // 10
    
        def reverse_list(x):
            if len(x) < 2:
                return x
            else:
                return reverse_list(x[len(x)//2:]) + reverse_list(x[:len(x)//2])
        
        
        if n < 0: return False
        else:
            add_to_list(n)
            lst_2 = reverse_list(x)
            
            for i, j in zip(x, lst_2):
                if i == j:
                    pass
                else:
                    return False
            return True
            
        
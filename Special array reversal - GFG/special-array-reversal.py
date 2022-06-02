#User function Template for python3

class Solution:
    def reverse(self, s):
        # code here
        start = 0
        end = len(s) - 1
        
        s = list(s)
        while start < end:
            if s[start].isalpha() and s[end].isalpha(): 
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            elif not s[end].isalpha() and not s[start].isalpha():
                end -= 1
                start += 1
            elif not s[start].isalpha():
                start += 1
            elif not s[end].isalpha():
                end -= 1
        
        return (''.join(s))

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        ob = Solution()
        ans = ob.reverse(s)
        print(ans)
# } Driver Code Ends
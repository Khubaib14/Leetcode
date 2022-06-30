#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        # code here
        stk = []
        result = ''
        i = 0
        while i < len(s):
            if not s[i].isdigit():
                stk.append(s[i])
                i += 1
            elif s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                stk.append(s[start:i])
            
        while stk:
            temp = stk.pop()
            result += temp
        return result 
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends
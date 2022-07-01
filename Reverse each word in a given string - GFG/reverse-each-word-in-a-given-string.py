#User function Template for python3

class Solution:
    def reverseWords(self, a):
        # code here
        stk = []
        result = ""
        for i in a:
            if i == ".":
                while stk:
                    result += stk[-1]
                    stk.pop()
                result += "."
            else:
                stk.append(i)
        while stk:
            result += stk[-1]
            stk.pop()
        return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
# } Driver Code Ends
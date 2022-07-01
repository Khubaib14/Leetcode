#User function Template for python3
class Solution:
    def valid(self, s): 
        #code here
        stk = []
        for i in s:
            if i in "([{":
                stk.append(i)
            elif i in ")}]":
                if len(stk) == 0:
                    return 0
                elif stk[-1] == "(" and i == ")":
                    stk.pop()
                elif stk[-1] == "{" and i == "}":
                    stk.pop()
                elif stk[-1] == "[" and i == "]":
                    stk.pop()
        if len(stk) != 0:
            return 0
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        if ob.valid(s):
            print(1)
        else:
            print(0)
# } Driver Code Ends
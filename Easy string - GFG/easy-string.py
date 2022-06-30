#User function Template for python3

class Solution:

    def transform(self, s):
        # code here 
        stk = []
        result = ''
        for i in s:
            if not stk:
                stk.append(i.lower())
            elif stk and stk[-1] == i.lower():
                stk.append(i.lower())
            elif stk[-1] != i.lower():
                result += str(len(stk)) + stk[-1]
                stk = []
                stk.append(i.lower())
        result += str(len(stk)) + stk[-1]
        return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        print(solObj.transform(S))
# } Driver Code Ends
#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        
        slow = 0
        fast = 0
        d = {}
        maxer = 0
        
        while fast <  len(s):
            d[s[fast]] = d.get(s[fast], 0) + 1
            
            if len(d) == k:
                maxer = max(maxer, fast-slow+1)
                # print(s[slow:fast+1])
            
            elif len(d) > k:
                while len(d) > k:
                    if d[s[slow]]:
                        d[s[slow]] -= 1
                        if d[s[slow]] == 0:
                            del d[s[slow]]
                    slow += 1
            fast += 1
            
        if maxer == 0:
            return -1
        else:
            return (maxer)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends
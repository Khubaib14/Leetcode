#User function Template for python3

class Solution:
    def smallestSubstring(self, s):
        # Code here
        slow = 0
        fast = 0
        miner = len(s)
        d = {}
        edge = False
        while fast < len(s):
            d[s[fast]] = d.get(s[fast], 0) + 1
            if len(d) == 3:
                miner = min(miner, (fast-slow+1))    
                while len(d) == 3:
                    edge = True
                    if d[s[slow]]:
                        d[s[slow]] -= 1
                        miner = min(miner, (fast-slow+1))
                        if d[s[slow]] == 0:
                            del d[s[slow]]
                    slow += 1
            fast += 1
        
        if not edge:
            return -1
        else:
            return (miner)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends
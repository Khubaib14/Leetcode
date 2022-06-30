#User function Template for python3
class Solution:
	def barcketNumbers(self, s):
		# code here
		stk = []
        result = []
        cnt = 0
        for i in s:
            if i == "(":
                cnt += 1
                stk.append(("(",cnt))
                result.append(stk[-1][1])
            elif i == ")" and stk and stk[-1][0] == "(":
                result.append(stk[-1][1])
                stk.pop()
        return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.barcketNumbers(S)
		for value in answer:
			print(value, end = " ")
		print()


# } Driver Code Ends
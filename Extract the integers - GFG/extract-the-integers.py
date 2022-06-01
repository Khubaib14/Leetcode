#User function Template for python3
import re
class Solution:

    def extractIntegerWords(self, s):
        # code here
       patt=re.compile('[0-9]+')
       k=patt.findall(s)
       #print(k)
       return k
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        if solObj.extractIntegerWords(s):
            print(*solObj.extractIntegerWords(s))
        else:
            print("No Integers")

# } Driver Code Ends
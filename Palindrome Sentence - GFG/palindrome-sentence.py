#User function Template for python3
class Solution:
	def sentencePalindrome(self, s):
		# your code here
		s = s.replace(" ","") #ignore white space
        ss =""
        for ch in s:
         if ch.isalpha():
             ss += ch
        
        i = 0 #left most index
        j = len(ss) -1
        
        while i <= j:
           if ss[i] != ss[j]:
               return 0
           
           elif ss[i] == ss[j]:
               i += 1
               j -= 1
        return 1
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		s = input ()
		ob = Solution()
		if ob.sentencePalindrome (s):
			print (1)
		else:
			print (0)
# } Driver Code Ends
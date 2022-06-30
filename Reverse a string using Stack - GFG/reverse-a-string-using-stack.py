#{ 
#Driver Code Starts

 # } Driver Code Ends
def reverse(s):
    
    #Add code here
    stk = []
    result = ''
    for i in s:
        stk.append(i)
    for _ in s:
        result += stk.pop()
    return result

#{ 
#Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
#} Driver Code Ends
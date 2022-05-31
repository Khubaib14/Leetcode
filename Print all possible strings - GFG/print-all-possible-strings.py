#Your task is to complete this function
#Function should print the required string
def Solve(ip, op="", ls=[]):
    if ip == "":
        ls.append(op)
        return ls
    op1 = op
    op2 = op
    
    op1 += ip[0]
    op2 = op2 + " " + ip[0]
    ip = ip[1:]
        
    Solve(ip, op1, ls)
    Solve(ip, op2, ls)
    
    return ls

def spaceString(ip):
    # Code here
    ls = []
    op = ip[0]
    return Solve(ip[1:], op, [])

#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        a = spaceString(arr)
        for _ in a:
            print(_,end="$")
        print ()
# } Driver Code Ends
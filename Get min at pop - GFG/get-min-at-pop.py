#User function Template for python3

#Function to push all the elements into the stack.

# Have implemented my own several times
def _push(a,n):

    # code here
    return a[::-1]

#Function to print minimum value in stack each time while popping.    
def _getMinAtPop(stack):
    
    # code here
    for i in range(len(stack)):
       n=min(stack)
       stack.pop(0)
       print(n,end=" ")
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        stack =  _push(a,n) # our stack to be used
        _getMinAtPop(stack) # print elements of stack as required
        print()

# } Driver Code Ends
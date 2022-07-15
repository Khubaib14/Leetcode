
#User function Template for python3


class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,mat, n): 
        # transpose
        for i in range(len(mat)):
            for j in range(i, len(mat)):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        # swapping the corresponding rows
        for i in range(len(mat)//2):
            mat[i], mat[len(mat)-1-i] = mat[len(mat)-1-i], mat[i]
        return mat

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        obj.rotateby90(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()

# } Driver Code Ends
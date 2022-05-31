// { Driver Code Starts
//Initial Template for Java
import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0)
        {
            int N=sc.nextInt();
			
            Solution ob = new Solution();
            ob.gfSeries(N);
            
        }
    }
}
// } Driver Code Ends


//User function Template for Java
class Solution{
    static long getnum(int N){
        if (N==1){
            return 0;
        }
        if (N==2){
            return 1;
        }
        return (long)(Math.pow(getnum(N-2), 2) - getnum(N-1));
    }
    static void gfSeries(int N){
        // code here
        for(int i=1;i<=N;i++){
            System.out.print(getnum(i)+" ");
        }
        System.out.println();
    }
}
// { Driver Code Starts
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends

class Solution{
    public:
    int findClosest(int arr[], int n, int target) 
    { 
        // Complete the function
        // Fucking tire
        int ans=INT_MAX,value=-1;
        for(int i=0;i<n;i++){
            int di=abs(arr[i]-target);
            if(di<=ans){
                ans=di;
                value=arr[i];
            }
        }
        return value;
    } 
};

// { Driver Code Starts.
int main()
{

    int t;
    cin>>t;
    while(t--)
    {
        int n,target;
        cin>>n>>target;
        int arr[n];
        for (int i=0; i<n; i++)
        {
            cin>>arr[i];
        }
        Solution ob;
        cout<<ob.findClosest(arr,n,target)<<endl;
    }
}
  // } Driver Code Ends
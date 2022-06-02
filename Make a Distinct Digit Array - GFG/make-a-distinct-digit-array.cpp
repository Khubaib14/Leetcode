// { Driver Code Starts

#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends

class Solution{
	public:
   	vector<int>  common_digits(vector<int>nums){
   	    // Code here
   	    map<int,int> mp;
   	    for(int i=0;i<nums.size();i++){
   	        while(nums[i]>0){
   	            mp[nums[i]%10]++;
   	            nums[i]/=10;
   	        }
   	        
   	    }
   	    vector<int> v;
   	    for(auto it:mp){
   	        v.push_back(it.first);
   	    }
   	    return v;
   	}    
};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n;
		cin >> n;
		vector<int>nums(n);
		for(int i = 0; i < nums.size(); i++)cin >> nums[i];
		Solution ob;
		vector<int> ans = ob.common_digits(nums);
		for(auto i: ans)
			cout << i << " ";
		cout << "\n";
	}  
	return 0;
}  // } Driver Code Ends
Approach 1: (Personal) Sliding Window: 2 pointers. Maxer for storing the longest array len, limit to account for allowance of one "0" char. Let fast move, decrement limit if 0 is encountered. Limit = 0 is okay. It means one 0 is there. This is acceptable. When a second 0 is encountered, limit becomes -1. This is when slow must be incremented. If slow encounters a "0", limit is incremented by 1. It will become 0, which is again acceptable.  We deduct 1 from fast - slow + 1 as we are accounting for one "0". Howver, there is one more decrement made, taking the expression to fast - slow - 1. I don't know why this works.
T: O(n)
S: O(1)
​
​
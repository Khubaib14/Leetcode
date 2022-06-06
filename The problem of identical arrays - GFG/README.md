# The problem of identical arrays
## Easy
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Two arrays of size N are called identical arrays if they contain the same elements. The order of elements in both arrays could be different; however,&nbsp;both the arrays must contain same elements. You are given two arrays of size N.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">You need to determine if the arrays are identical or not.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span><br style="user-select: auto;">
&nbsp;</p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input :</strong> A[] = {1, 2, 3, 4, 5}, B[] = {3, 4, 1, 2, 5}
<strong style="user-select: auto;">Output :</strong> 1
<strong style="user-select: auto;">Explanation:</strong>
Here we can see array A[] = [1, 2, 3, 4, 5] and 
B[] = [3, 4, 1, 2, 5]. If we look both the array then we 
can get that array B is the permutation of A. So, both array
are identical. </span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input :</strong> A[] = {1, 2, 4}, B[] = {3, 2, 1} <strong style="user-select: auto;">
Output :</strong> 0 </span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <strong style="user-select: auto;">check()</strong> that takes an array <strong style="user-select: auto;">(arr)</strong>, another array <strong style="user-select: auto;">(brr)</strong>,&nbsp;size of both array&nbsp;<strong style="user-select: auto;">(n)</strong>, and return the 1 if both the array are identical else 0. The driver code takes care of the printing.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong>&nbsp;O(NLog(N)).<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong>&nbsp;O(1).</span><br style="user-select: auto;">
&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 ≤ N ≤ 10<sup style="user-select: auto;">5</sup><br style="user-select: auto;">
0 ≤ A[i] ≤ 9</span></p>
 <p style="user-select: auto;"></p>
            </div>
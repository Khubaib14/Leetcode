# Pair with given sum in a sorted array
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 20px; user-select: auto;">You are given an array <strong style="user-select: auto;">Arr</strong> of size <strong style="user-select: auto;">N</strong>. You need to find <strong style="user-select: auto;">all pairs</strong> in the array that sum to a number <strong style="user-select: auto;">K</strong>. If no such pair exists then output will be <strong style="user-select: auto;">-1</strong>. The elements of the array are <strong style="user-select: auto;">distinct </strong>and are in <strong style="user-select: auto;">sorted </strong>order.<br style="user-select: auto;">
<strong style="user-select: auto;">Note:</strong> (a,b) and (b,a) are considered same. Also, an element cannot pair with itself, i.e., (a,a) is invalid.</span></p>

<p style="user-select: auto;"><span style="font-size: 20px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 20px; user-select: auto;"><strong style="user-select: auto;">â€‹</strong><strong style="user-select: auto;">Input:
</strong>n = 7
arr[] = {1, 2, 3, 4, 5, 6, 7}
K = 8
<strong style="user-select: auto;">Output:
</strong>3
<strong style="user-select: auto;">Explanation:</strong>
We find 3 such pairs that
sum to 8 (1,7) (2,6) (3,5)
</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 20px; user-select: auto;"><strong style="user-select: auto;">â€‹Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 20px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>n = 7
arr[] = {1, 2, 3, 4, 5, 6, 7}
K = 98 <strong style="user-select: auto;">
Output:
</strong>-1 </span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 20px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <strong style="user-select: auto;">Countpair()</strong> that takes an array <strong style="user-select: auto;">(arr)</strong>, sizeOfArray <strong style="user-select: auto;">(n)</strong>, an integer <strong style="user-select: auto;">K</strong> and return the count of the pairs which add up to the sum <strong style="user-select: auto;">K</strong>. The driver code takes care of the printing.</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 20px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong>&nbsp;O(N).<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong>&nbsp;O(1).</span></p>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 20px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
0 &lt;= A<sub style="user-select: auto;">i</sub> &lt;=10<sup style="user-select: auto;">7</sup><br style="user-select: auto;">
2 &lt;= N &lt;= 10<sup style="user-select: auto;">7</sup><br style="user-select: auto;">
0 &lt;= K &lt;= 10<sup style="user-select: auto;">7</sup></span></p>
 <p style="user-select: auto;"></p>
            </div>
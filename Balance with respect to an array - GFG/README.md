# Balance with respect to an array
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">As a programmer, it is very necessary to maintain balance in the life.<br style="user-select: auto;">
Here is task for you to maintain a balance. Your task is to find whether a given number <strong style="user-select: auto;">x</strong> is balanced with respect to a given array <strong style="user-select: auto;">a[ ]</strong>&nbsp;which is sorted in&nbsp;non-decreasing order.<br style="user-select: auto;">
Given a sorted array <strong style="user-select: auto;">a[ ],</strong> the ceiling of <strong style="user-select: auto;">x</strong>&nbsp;is the smallest element in the array greater than or equal to <strong style="user-select: auto;">x</strong>, and the floor of <strong style="user-select: auto;">x</strong> is the greatest element smaller than or equal to <strong style="user-select: auto;">x</strong>. The number '<strong style="user-select: auto;">x</strong>' is said to be balanced if the absolute difference between&nbsp;floor of <strong style="user-select: auto;">x</strong> and <strong style="user-select: auto;">x</strong> is equal to the absolute difference between&nbsp;ceil of <strong style="user-select: auto;">x</strong> and <strong style="user-select: auto;">x</strong> <em style="user-select: auto;">i.e</em>. if <strong style="user-select: auto;">absolute(x - floor(x, a[])) = absolute(ceil(x, a[]) - x)</strong>.<br style="user-select: auto;">
If one of floor or ceil does not exist assume '<strong style="user-select: auto;">x</strong>' to be balanced.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>N = 7  
x = 5
a[] = {1, 2, 8, 10, 10, 12, 19} 
<strong style="user-select: auto;">Output:</strong> 
Balanced
<strong style="user-select: auto;">Explanation</strong>: Here 2 is the floor value and 
8 is the ceil value and (5 - 2) = (8 - 5).  </span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>N = 8  
x = 9 
a[] = {1, 2, 5, 7, 8, 11, 12, 15} 
<strong style="user-select: auto;">Output:</strong> 
Not Balanced</span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <strong style="user-select: auto;">FindElement</strong>() that takes <strong style="user-select: auto;">array a[ ], its size N&nbsp;</strong>and<strong style="user-select: auto;"> integer x</strong>&nbsp;as input parameters and returns the string "<strong style="user-select: auto;">Balanced</strong>"&nbsp;if the absolute difference between&nbsp;floor of x and x is equal to the absolute difference between&nbsp;ceil of x and x or else returns string "<strong style="user-select: auto;">Not Balanced</strong>".</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong> O(LogN)<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong> O(1)</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 ≤ N ≤ 10<sup style="user-select: auto;">6</sup></span></p>
 <p style="user-select: auto;"></p>
            </div>
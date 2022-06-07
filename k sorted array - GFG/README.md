# k sorted array
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given an array of&nbsp;<strong style="user-select: auto;">n</strong>&nbsp;distinct elements. Check whether the given array is a&nbsp;<strong style="user-select: auto;">k</strong>&nbsp;sorted array or not. A&nbsp;<strong style="user-select: auto;">k</strong>&nbsp;sorted array is an array where each element is at most&nbsp;<strong style="user-select: auto;">k</strong>&nbsp;distance away from its target position in the sorted array.</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>N=6
arr[] = {3, 2, 1, 5, 6, 4} 
K = 2
<strong style="user-select: auto;">Output:</strong> Yes
<strong style="user-select: auto;">Explanation</strong>:
Every element is at most <strong style="user-select: auto;">2</strong> distance 
away from its target position in the
sorted array.  </span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>N=7
arr[] = {13, 8, 10, 7, 15, 14, 12}
K = 1
<strong style="user-select: auto;">Output:</strong> No</span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <strong style="user-select: auto;">isKSortedArray</strong>() that takes <strong style="user-select: auto;">array arr, integer&nbsp;n and integer k</strong> as parameters and return&nbsp;"Yes" if the array is a k sorted array else return "No".</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong> O(NlogN).<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong> O(N).</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 ≤ N ≤ 10<sup style="user-select: auto;">5</sup><br style="user-select: auto;">
0 ≤ K ≤ N</span></p>
 <p style="user-select: auto;"></p>
            </div>
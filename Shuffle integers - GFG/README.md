# Shuffle integers
## Easy
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given an array <strong style="user-select: auto;">arr[]</strong> of <strong style="user-select: auto;">n</strong> elements in the following format {a1, a2, a3, a4, .., an/2, b1, b2, b3, b4, ., bn/2}, the task is shuffle the array to {a1, b1, a2, b2, a3, b3, , an/2, bn/2} without using extra space.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input: </strong>n = 4, arr[] = {1, 2, 9, 15}
<strong style="user-select: auto;">Output:</strong>  1 9 2 15
<strong style="user-select: auto;">Explanation</strong>: a1=1 , a2=2 , b1=9 , b2=15
So the final array will be :  
a1, b1, a2, b2 = { 1, 9, 2, 15 }

<strong style="user-select: auto;">Example 2:</strong>
<strong style="user-select: auto;">Input: </strong>n = 6
arr[] = {1, 2, 3, 4, 5, 6}
<strong style="user-select: auto;">Output:</strong> 1 4 2 5 3 6</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <strong style="user-select: auto;">shuffleArray</strong>() that takes array<strong style="user-select: auto;"> arr[], </strong>and an integer<strong style="user-select: auto;"> n</strong>&nbsp;as parameters and modifies the given array according to the above-given pattern.</span></p>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong> O(n).<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong> O(n).</span></p>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 ≤ n ≤ 10<sup style="user-select: auto;">5</sup><br style="user-select: auto;">
-10<sup style="user-select: auto;">5</sup>≤ arr<sub style="user-select: auto;">i</sub>&nbsp;≤ 10<sup style="user-select: auto;">5</sup></span></p>
 <p style="user-select: auto;"></p>
            </div>
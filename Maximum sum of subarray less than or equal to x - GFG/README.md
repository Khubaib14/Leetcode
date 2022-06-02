# Maximum sum of subarray less than or equal to x
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given an array <strong style="user-select: auto;">arr[]</strong> of integers of size <strong style="user-select: auto;">N</strong> and a number <strong style="user-select: auto;">X</strong>, the task is to find the sum of subarray having maximum sum less than or equal to the given value of <strong style="user-select: auto;">X</strong>.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="user-select: auto; position: relative;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input: </strong>N = 5, X = 11
arr[] = {1, 2, 3, 4, 5} 
<strong style="user-select: auto;">Output:</strong>  10
<strong style="user-select: auto;">Explanation</strong>: Subarray having maximum 
sum is {1, 2, 3, 4}.</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">&nbsp;<br style="user-select: auto;">
<strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="user-select: auto; position: relative;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input: </strong>N = 5, X = 7
arr[] = {2, 4, 6, 8, 10} 
<strong style="user-select: auto;">Output:</strong> &nbsp;6
<strong style="user-select: auto;">Explanation:</strong> Subarray having maximum 
sum is {2, 4} or {6}.</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <strong style="user-select: auto;">calculateMaxSumLength</strong>() that takes array <strong style="user-select: auto;">arr, </strong>integer <strong style="user-select: auto;">N</strong>, and integer<strong style="user-select: auto;"> X&nbsp;</strong>as parameters and returns maximum sum of any subarray that is less than or equal to x.</span></p>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong> O(N).&nbsp;<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong> O(1).</span></p>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 ≤ N ≤ 10<sup style="user-select: auto;">6</sup></span></p>
 <p style="user-select: auto;"></p>
            </div>
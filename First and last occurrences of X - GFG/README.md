# First and last occurrences of X
## Easy
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given a sorted array having <strong style="user-select: auto;">N&nbsp;</strong>elements,&nbsp;find the indices&nbsp;of the first and last occurrences of an element <strong style="user-select: auto;">X</strong>&nbsp;in the given array.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Note:</strong> If the number <strong style="user-select: auto;">X&nbsp;</strong>is not found in the array, return '-1' as an array.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong>
N = 4 , X = 3
arr[] = { 1, 3, 3, 4 }
<strong style="user-select: auto;">Output:</strong>
1 2
<strong style="user-select: auto;">Explanation:</strong>
For the above array, first occurence
of <strong style="user-select: auto;">X = 3 </strong>is at <strong style="user-select: auto;">index = 1</strong> and last
occurence is at <strong style="user-select: auto;">index = 2</strong>.</span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong>
N = 4, X = 5
arr[] = { 1, 2, 3, 4 }
<strong style="user-select: auto;">Output:</strong>
-1
<strong style="user-select: auto;">Explanation: </strong>
As 5 is not present in the array,
so the answer is -1.</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
You don't need to read input or print anything. Complete the function <strong style="user-select: auto;">firstAndLast</strong><strong style="user-select: auto;">()</strong> that takes the array <strong style="user-select: auto;">arr</strong>, its size <strong style="user-select: auto;">N&nbsp;</strong>and the value <strong style="user-select: auto;">X&nbsp;</strong>as input parameters and returns a list of integers containing the indices of first and last occurence of&nbsp;<strong style="user-select: auto;">X.</strong></span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong> O(log(N))<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong> O(1)</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:&nbsp;</strong><br style="user-select: auto;">
1 &lt;= N &lt;= 10^5&nbsp;</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">0 &lt;= arr[i], X &lt;= 10<sup style="user-select: auto;">9</sup></span></p>
 <p style="user-select: auto;"></p>
            </div>
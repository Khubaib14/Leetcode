# Searching an element in a sorted array
## Easy
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given an array&nbsp;<strong style="user-select: auto;">arr[] </strong>sorted in ascending order of size <strong style="user-select: auto;">N</strong> and an integer <strong style="user-select: auto;">K</strong>. Check if K&nbsp;is present in the array or not.</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>N = 5, K = 6
arr[] = {1,2,3,4,6}
<strong style="user-select: auto;">Output: </strong>1<strong style="user-select: auto;">
Exlpanation: </strong>Since, 6 is present in 
the array at index 4 (0-based indexing),
output is 1.</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>N = 5, K = 2
arr[] = {1,3,4,5,6}
<strong style="user-select: auto;">Output: </strong>-1<strong style="user-select: auto;">
Exlpanation: </strong>Since, 2 is not present 
in the array, output is -1.</span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
You don't need to read input or print anything. Complete the function&nbsp;<strong style="user-select: auto;">searchInSorted()</strong> which takes the sorted array arr[], its size N and the element K as input parameters&nbsp;and returns 1 if K&nbsp;is present in the array, else it returns -1.&nbsp;</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:&nbsp;</strong>O(Log N)<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:&nbsp;</strong>O(1)</span></p>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 &lt;= N &lt;= 10<sup style="user-select: auto;">6</sup><br style="user-select: auto;">
1 &lt;= K &lt;= 10<sup style="user-select: auto;">6</sup><br style="user-select: auto;">
1 &lt;= arr[i] &lt;= 10<sup style="user-select: auto;">6</sup></span></p>

<p style="user-select: auto;">&nbsp;</p>
 <p style="user-select: auto;"></p>
            </div>
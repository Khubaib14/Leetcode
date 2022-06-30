# Immediate Smaller Element
## Easy
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given an integer array <strong style="user-select: auto;">Arr</strong> of size <strong style="user-select: auto;">N</strong>. For each element in the array, check whether the right adjacent element (on the&nbsp;next&nbsp;immediate position) of the array is smaller. If next element is smaller, update the current index to that element.&nbsp;If not, then&nbsp;&nbsp;<strong style="user-select: auto;">-1</strong>.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>N = 5
Arr[] = {4, 2, 1, 5, 3}
<strong style="user-select: auto;">Output:</strong>
2 1 -1 3 -1
<strong style="user-select: auto;">Explanation:</strong> Array elements are 4, 2, 1, 5
3. Next to 4 is 2 which is smaller, so we
print 2. Next of 2 is 1 which is smaller,
so we print 1. Next of 1 is 5 which is
greater, so we print -1. Next of 5 is 3
which is smaller, so we print 3.&nbsp; Note
that for last element, output is always 
going to be -1 because there is no element
on right.</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>N = 6
Arr[] = {5, 6, 2, 3, 1,&nbsp;7}
<strong style="user-select: auto;">Output:</strong>
-1 2 -1 1 -1 -1
<strong style="user-select: auto;">Explanation: </strong>Next to 5 is 6 which is
greater, so we print -1.Next of 6 is 2
which is smaller, so we print 2. Next
of 2 is 3 which is greater, so we
print -1. Next of 3 is 1 which is
smaller, so we print 1. Next of 1 is
7 which is greater, so we print -1.
Note that for last element, output is
always going to be -1 because there is
no element on right.</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:&nbsp;&nbsp;</strong><br style="user-select: auto;">
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong style="user-select: auto;">immediateSmaller()</strong>&nbsp;which takes the&nbsp;array of&nbsp;integers&nbsp;<strong style="user-select: auto;">arr&nbsp;</strong>and&nbsp;<strong style="user-select: auto;">n</strong><strong style="user-select: auto;">&nbsp;</strong>as parameters. You need to change the array itself.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong>&nbsp;O(N)<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 ≤ N ≤ 10<sup style="user-select: auto;">7</sup><br style="user-select: auto;">
1 ≤ Arr[i] ≤ 10<sup style="user-select: auto;">5</sup></span></p>

<p style="user-select: auto;">&nbsp;</p>
 <p style="user-select: auto;"></p>
            </div>
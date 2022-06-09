# Selection Sort
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Example 1:</span></strong></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong>
N = 5
arr[] = {4, 1, 3, 9, 7}</span>
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Output:</strong>
1 3 4 7 9</span>
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Explanation:</strong>
Maintain sorted (in bold) and unsorted subarrays.
Select 1. Array becomes <strong style="user-select: auto;">1</strong> 4 3 9 7.
Select 3. Array becomes <strong style="user-select: auto;">1 3</strong> 4 9 7.
Select 4. Array becomes <strong style="user-select: auto;">1 3 4</strong> 9 7.
Select 7. Array becomes <strong style="user-select: auto;">1 3 4 7</strong> 9.
Select 9. Array becomes <strong style="user-select: auto;">1 3 4 7 9</strong>.</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Example 2:</span></strong></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong>
N = 10
arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}</span>
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Output:</strong>
1 2 3 4 5 6 7 8 9 10</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task: &nbsp;</strong><br style="user-select: auto;">
You dont need to read input or print anything. Complete the functions&nbsp;<strong style="user-select: auto;">select() and selectionSort()</strong>&nbsp;,where select() takes arr[] and starting point of unsorted array i as input parameters and returns the selected element for each iteration in selection sort, and selectionSort() takes the array and it's size and sorts the array.</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity: </strong>O(N<sup style="user-select: auto;">2</sup>)<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space: </strong>O(1)</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 ≤ N ≤ 10^3</span></p>
 <p style="user-select: auto;"></p>
            </div>
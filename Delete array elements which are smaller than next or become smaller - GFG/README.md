# Delete array elements which are smaller than next or become smaller
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given an array arr[] and a number k. The task is to delete <strong style="user-select: auto;">k</strong> elements which are smaller than next element (i.e., we delete arr[i] if arr[i] &lt; arr[i+1]) or become smaller than next because next element is deleted.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="user-select: auto; position: relative;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">â€‹Input :</strong> arr[ ] = {20, 10, 25, 30, 40} 
        and K = 2
<strong style="user-select: auto;">Output :</strong> 25 30 40
<strong style="user-select: auto;">Explanation:</strong>
First we delete 10 because it follows&nbsp;
arr[i] &lt; arr[i+1]. Then we delete 20 
because 25 is moved next to it and it 
also starts following the condition.
</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">â€‹Example 2:</strong></span></p>

<pre style="user-select: auto; position: relative;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input :</strong> arr[ ] = {3, 100, 1} and K = 1<strong style="user-select: auto;">
Output :</strong>  100 1 </span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <strong style="user-select: auto;">deleteElement()</strong> that takes an array <strong style="user-select: auto;">(arr)</strong>, sizeOfArray <strong style="user-select: auto;">(n)</strong>, an integer <strong style="user-select: auto;">K</strong> and return the array arr[] after deleting the k elements from the array if possible, else print the left array as it is. The driver code takes care of the printing.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong>&nbsp;O(N).<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong>&nbsp;O(N).</span></p>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
2 ≤ N ≤ 10<sup style="user-select: auto;">5</sup><br style="user-select: auto;">
1 ≤ K &lt;&nbsp;N&nbsp;</span></p>
 <p style="user-select: auto;"></p>
            </div>
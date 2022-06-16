# Counting elements in two arrays
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given two unsorted arrays <strong style="user-select: auto;">arr1[]</strong> and <strong style="user-select: auto;">arr2[]</strong>. They may contain duplicates. For each element in arr1[] count elements less than or equal to it in array arr2[].</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>m = 6, n = 6
arr1[] = {1,2,3,4,7,9}
arr2[] = {0,1,2,1,1,4}
<strong style="user-select: auto;">Output: </strong>4 5 5 6 6 6<strong style="user-select: auto;">
Explanation: </strong>Number of&nbsp;elements less than
or equal to 1, 2, 3, 4, 7, and 9 in the
second array are respectively 4,5,5,6,6,6</span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>m = 5, n = 7
arr1[] = {4 8 7 5 1}
arr2[] = {4,48,3,0,1,1,5}
<strong style="user-select: auto;">Output: </strong>5 6 6 6 3</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task :</strong><br style="user-select: auto;">
Complete the function&nbsp;<strong style="user-select: auto;">countEleLessThanOrEqual()&nbsp;</strong>that takes two array arr1[], arr2[],&nbsp;&nbsp;m, and n&nbsp;as input and returns an array containing the required results(the count of elements less than or equal to it in arr2 for each element in arr1 where i<sub style="user-select: auto;">th</sub> output represents the count for i<sub style="user-select: auto;">th</sub> element in arr1.)</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong>&nbsp;O((m + n) * log n).<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong>&nbsp;O(1).</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1&lt;=m,n&lt;=10^5<br style="user-select: auto;">
1&lt;=arr1[i],arr2[j]&lt;=10^5</span></p>
 <p style="user-select: auto;"></p>
            </div>
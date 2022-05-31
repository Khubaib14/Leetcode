# Print Pattern
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Print a sequence of numbers starting with <strong style="user-select: auto;">N</strong>&nbsp;where A[0] = N, <strong style="user-select: auto;"><em style="user-select: auto;">without using loop</em></strong>, in which&nbsp; A[i+1] = A[i] - 5,&nbsp; until A[i] &gt; 0.&nbsp;After that&nbsp;A[i+1] = A[i] + 5&nbsp; repeat it until A[i] = N.</span></p>

<p style="user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Example 1:</span></strong></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong> N = 16
<strong style="user-select: auto;">Output:</strong> 16 11 6 1 -4 1 6 11 16
<strong style="user-select: auto;">Explaination:</strong> The value decreses until it 
is greater than 0. After that it increases 
and stops when it becomes 16 again.</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Example 2:</span></strong></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong> N = 10
<strong style="user-select: auto;">Output:</strong> 10 5 0 5 10
<strong style="user-select: auto;">Explaination:</strong> It follows the same logic as 
per the above example.</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
You do not need to read input or print anything. Your task is to complete the function <strong style="user-select: auto;">pattern()</strong> which takes N as input parameters and returns a list containing the pattern.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong> O(N)<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong> O(N)</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 ≤ N ≤ 10<sup style="user-select: auto;">4</sup>&nbsp;</span></p>
 <p style="user-select: auto;"></p>
            </div>
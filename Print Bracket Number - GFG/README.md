# Print Bracket Number
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given a string S, the task is to find the bracket numbers.&nbsp;</span></p>

<p style="user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Example 1:</span></strong></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong>  S = "(aa(bdc))p(dee)</span><span style="font-size: 20px; user-select: auto;">â€‹</span><span style="font-size: 18px; user-select: auto;">"
<strong style="user-select: auto;">Output:</strong> 1 2 2 1 3 3
<strong style="user-select: auto;">Explanation:</strong> The highlighted brackets in
the given string <strong style="user-select: auto;">(</strong>aa<strong style="user-select: auto;">(</strong>bdc<strong style="user-select: auto;">))</strong>p<strong style="user-select: auto;">(</strong>dee<strong style="user-select: auto;">)</strong> has been 
assigned the numbers as: 1 2 2 1 3 3.</span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Example 2:</span></strong></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong>  S = "(((()("
<strong style="user-select: auto;">Output:</strong> 1 2 3 4 4 5
<strong style="user-select: auto;">Explanation:</strong> The highlighted brackets in
the given string <strong style="user-select: auto;">(((()(</strong> has been assigned
the numbers as: 1 2 3 4 4 5</span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<div style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">User Task:</strong><br style="user-select: auto;">
Your task is to complete the function <strong style="user-select: auto;"><code style="user-select: auto;">barcketNumbers</code>()&nbsp;</strong>which takes a single string as input and returns a list of numbers. You do not need to take any input or print anything.</span></div>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:&nbsp;</strong>O(|S|)<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:&nbsp;</strong>O(|S|)</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 &lt;= |S| &lt;= 10<sup style="user-select: auto;">5</sup></span><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;">S contains lower case English alphabets, and '(', ')' characters<br style="user-select: auto;">
At any time the number of opening brackets are greater than closing brackets</span></p>
 <p style="user-select: auto;"></p>
            </div>
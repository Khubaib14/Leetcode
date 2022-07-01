# Restrictive Candy Crush
## Medium 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given a string <strong style="user-select: auto;">s</strong>&nbsp;and an integer <strong style="user-select: auto;">k</strong>, the task is to reduce the string by applying the following operation:<br style="user-select: auto;">
Choose a group of <strong style="user-select: auto;">k</strong>&nbsp;consecutive identical characters and remove them.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">The operation can be performed any number of times until it is no longer possible.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>k = 2
s = "geeksforgeeks"
<strong style="user-select: auto;">Output:</strong>
gksforgks
<strong style="user-select: auto;">Explanation:</strong>
Modified String after each step: 
<strong style="user-select: auto;">"</strong>g<strong style="user-select: auto;">ee</strong>ksforg<strong style="user-select: auto;">ee</strong>ks" -&gt; "gksforgks"</span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>k = 2
s =<strong style="user-select: auto;"> "</strong>geegsforgeeeks" 
<strong style="user-select: auto;">Output:</strong>
sforgeks
<strong style="user-select: auto;">Explanation:</strong>
Modified String after each step:
<strong style="user-select: auto;">"</strong>g<strong style="user-select: auto;">ee</strong>gsforg<strong style="user-select: auto;">eee</strong>ks" -&gt; "<strong style="user-select: auto;">gg</strong>sforgeks" -&gt; "sforgeks"</span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task: </strong>&nbsp;<br style="user-select: auto;">
You don't need to read input or print anything. Complete the function <strong style="user-select: auto;">Reduced_String()</strong> which takes integer <strong style="user-select: auto;">k</strong> and string&nbsp;<strong style="user-select: auto;">s</strong>&nbsp;as input parameters and returns the reduced string.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong> O(|s|)<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong> O(|s|)</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 ≤ |s|&nbsp;≤ 10<sup style="user-select: auto;">5</sup><br style="user-select: auto;">
1&nbsp;≤ k&nbsp;≤ |s|</span></p>
 <p style="user-select: auto;"></p>
            </div>
# Akku and Binary Numbers
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Akku likes binary numbers and she likes playing with these numbers. Her teacher once gave her a question.For given value of&nbsp; L and&nbsp;R, Akku have to find the count of number X, which have only three-set bits in it's binary representation such that "L ≤ X ≤ R".Akku is genius, she solved the problem easily. Can you do it ??</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input</strong>:
L = 11 and R = 19 
<strong style="user-select: auto;">Output:</strong>&nbsp;4
<strong style="user-select: auto;">Explanation</strong>:
There are 4 such numbers with 3 set bits in 
range 11 to 19.
11 -&gt; 1011
13 -&gt; 1101
14 -&gt; 1110
19 -&gt; 10011</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong>
L = 14 and R = 19
<strong style="user-select: auto;">Output: </strong>2
</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:&nbsp;&nbsp;</strong><br style="user-select: auto;">
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong style="user-select: auto;">solve()</strong>&nbsp;which takes the integer <strong style="user-select: auto;">L</strong> and <strong style="user-select: auto;">R</strong> as input parameters and returns&nbsp;the count of number X, which have only three-set bits in its binary representation such that "L ≤ X ≤ R".<br style="user-select: auto;">
<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Time Complexity:</strong> O(log(63<sup style="user-select: auto;">3</sup>))<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong> O(1)</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></span><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;">1 ≤ L ≤ R ≤ 10<sup style="user-select: auto;">18</sup></span></p>
 <p style="user-select: auto;"></p>
            </div>
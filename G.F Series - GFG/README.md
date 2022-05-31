# G.F Series
## Easy
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Siddhant made a special series and named it as G.F Series. The series follows this trend &nbsp;Tn=(Tn-2)2-(Tn-1) &nbsp;in which the first and the second term are 0 and 1 respectively. Help Siddhant to find up to N terms of the series.</span></p>

<p style="user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Example 1:</span></strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Input:
</span></strong><span style="font-size: 18px; user-select: auto;">N = 3</span>
<strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Output:
</span></strong><span style="font-size: 18px; user-select: auto;">0 1 -1</span>
<strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Explanation:
</span></strong><span style="font-size: 18px; user-select: auto;">First-term is given as 0 and the second 
term is 1. So the T3 = (T<sub style="user-select: auto;">3-2</sub>)<sup style="user-select: auto;">2</sup> - (T<sub style="user-select: auto;">3-1</sub>) 
= T<sub style="user-select: auto;">1</sub><sup style="user-select: auto;">2</sup> - T<sub style="user-select: auto;">2</sub> = 0<sup style="user-select: auto;">2</sup> - 1 = -1</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Example 2:</span></strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Input:
</span></strong><span style="font-size: 18px; user-select: auto;">N = 6</span>
<strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Output:
</span></strong><span style="font-size: 18px; user-select: auto;">0 1 -1 2 -1 5  </span>
<strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Explanation:
</span></strong><span style="font-size: 18px; user-select: auto;">first term : 0
second term : 1
third term : -1
fourth term = (1)<sup style="user-select: auto;">2</sup> - (-1) = 2
fifth term = (-1)<sup style="user-select: auto;">2</sup> - (2) = 1 - 2 = -1
sixth term = (2)<sup style="user-select: auto;">2</sup> - (-1) = 4 + 1 = 5 </span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:&nbsp;&nbsp;</strong></span><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;">You don't need to read input. Your task is to complete the function&nbsp;</span><strong style="user-select: auto;">gfSeries</strong><span style="font-size: 18px; user-select: auto;">()&nbsp;which takes an integer N as an input parameter and print first N term of the series.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity</strong>:&nbsp;O(N)<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong>&nbsp;O(N)</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 &lt;= N&nbsp;&lt;= 15</span></p>

<p style="user-select: auto;">&nbsp;</p>
 <p style="user-select: auto;"></p>
            </div>
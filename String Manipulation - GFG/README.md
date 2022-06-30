# String Manipulation
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><div class="starwars-lab" style="user-select: auto;">
<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><span style="font-family: arial, helvetica, sans-serif; user-select: auto;">Tom is a string freak. He has got sequences of&nbsp; n words to manipulate. If in a sequence, two same words come together then hell destroy each other. He wants to know the number of words left in the sequence after this pairwise destruction.</span></span><br style="user-select: auto;">
&nbsp;</p>

<div class="starwars-lab" style="user-select: auto;">
<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><span style="font-family: arial, helvetica, sans-serif; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><span style="font-family: arial, helvetica, sans-serif; user-select: auto;"><strong style="user-select: auto;">Input:</strong>
5
v[] = {"ab", "aa", "aa", "bcd", "ab"}
<strong style="user-select: auto;">Output:</strong>
3<strong style="user-select: auto;">
Explanation:</strong>
ab aa aa bcd ab
After the first iteration, we'll have: ab bcd ab
We can't further destroy more strings and
hence we stop and the result is 3. </span></span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><span style="font-family: arial, helvetica, sans-serif; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><span style="font-family: arial, helvetica, sans-serif; user-select: auto;"><strong style="user-select: auto;">Input:</strong>
4
v[] = {"tom", "jerry", "jerry", "tom"}
<strong style="user-select: auto;">Output:</strong>
0
<strong style="user-select: auto;">Explanation:
</strong>tom jerry jerry tom
After the first iteration, we'll have: tom tom
After the second iteration: 'empty-array' 
Hence, the result is 0. </span></span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>
</div>

<p style="user-select: auto;"><br style="user-select: auto;">
&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><span style="font-family: arial, helvetica, sans-serif; user-select: auto;"><strong style="user-select: auto;">Your Task:&nbsp;&nbsp;</strong><br style="user-select: auto;">
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong style="user-select: auto;">removeConsecutiveSame()</strong>&nbsp;which takes the array <strong style="user-select: auto;">A[]</strong> and its size <strong style="user-select: auto;">N</strong><strong style="user-select: auto;"> </strong>as inputs and returns the number of words left per sequence.</span></span></p>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><span style="font-family: arial, helvetica, sans-serif; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity: </strong>O(N)<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space: </strong>O(N)<br style="user-select: auto;">
<br style="user-select: auto;">
<br style="user-select: auto;">
<strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 ≤ N ≤ 100<br style="user-select: auto;">
1 ≤ |S<sub style="user-select: auto;">i</sub>| ≤ 50</span></span></p>
</div>
 <p style="user-select: auto;"></p>
            </div>
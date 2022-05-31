# Print all possible strings
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given a string <strong style="user-select: auto;">str</strong> your task is to complete the function<strong style="user-select: auto;">&nbsp;spaceString</strong> which takes only one argument the string<strong style="user-select: auto;"> str </strong>and&nbsp;&nbsp;finds all possible strings that can be made by placing spaces (zero or one) in between them.&nbsp;<br style="user-select: auto;">
<br style="user-select: auto;">
For eg . &nbsp;for the string abc all valid strings will be<br style="user-select: auto;">
&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;abc<br style="user-select: auto;">
&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ab c<br style="user-select: auto;">
&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;a bc<br style="user-select: auto;">
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; a b c<br style="user-select: auto;">
<br style="user-select: auto;">
<strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>str = abc
<strong style="user-select: auto;">Output: </strong>abc$ab&nbsp;c$a bc$a b c$<strong style="user-select: auto;">
</strong></span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>str = xy
<strong style="user-select: auto;">Output: </strong>xy$x y$

</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
Complete the function&nbsp;<strong style="user-select: auto;">spaceString()&nbsp;</strong>which takes a character array as an input parameter and returns list of all possible answers. The driver code will print the all possible answer '$' separated</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong>&nbsp;O(N * 2<sup style="user-select: auto;">N</sup>)<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong>&nbsp;O(N)</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1&lt;= length of string str&nbsp;&lt;=10<br style="user-select: auto;">
<br style="user-select: auto;">
<strong style="user-select: auto;">Note:</strong>The <strong style="user-select: auto;">Input/Ouput</strong> format and <strong style="user-select: auto;">Example</strong> given are used for system's internal purpose, and should be used by a user for <strong style="user-select: auto;">Expected Output</strong> only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.</span></p>
 <p style="user-select: auto;"></p>
            </div>
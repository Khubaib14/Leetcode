<h2><a href="https://leetcode.com/problems/reverse-prefix-of-word/">2000. Reverse Prefix of Word</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given a <strong style="user-select: auto;">0-indexed</strong> string <code style="user-select: auto;">word</code> and a character <code style="user-select: auto;">ch</code>, <strong style="user-select: auto;">reverse</strong> the segment of <code style="user-select: auto;">word</code> that starts at index <code style="user-select: auto;">0</code> and ends at the index of the <strong style="user-select: auto;">first occurrence</strong> of <code style="user-select: auto;">ch</code> (<strong style="user-select: auto;">inclusive</strong>). If the character <code style="user-select: auto;">ch</code> does not exist in <code style="user-select: auto;">word</code>, do nothing.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, if <code style="user-select: auto;">word = "abcdefd"</code> and <code style="user-select: auto;">ch = "d"</code>, then you should <strong style="user-select: auto;">reverse</strong> the segment that starts at <code style="user-select: auto;">0</code> and ends at <code style="user-select: auto;">3</code> (<strong style="user-select: auto;">inclusive</strong>). The resulting string will be <code style="user-select: auto;">"<u style="user-select: auto;">dcba</u>efd"</code>.</li>
</ul>

<p style="user-select: auto;">Return <em style="user-select: auto;">the resulting string</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> word = "<u style="user-select: auto;">abcd</u>efd", ch = "d"
<strong style="user-select: auto;">Output:</strong> "<u style="user-select: auto;">dcba</u>efd"
<strong style="user-select: auto;">Explanation:</strong>&nbsp;The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> word = "<u style="user-select: auto;">xyxz</u>xe", ch = "z"
<strong style="user-select: auto;">Output:</strong> "<u style="user-select: auto;">zxyx</u>xe"
<strong style="user-select: auto;">Explanation:</strong>&nbsp;The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> word = "abcd", ch = "z"
<strong style="user-select: auto;">Output:</strong> "abcd"
<strong style="user-select: auto;">Explanation:</strong>&nbsp;"z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= word.length &lt;= 250</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">word</code> consists of lowercase English letters.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">ch</code> is a lowercase English letter.</li>
</ul>
</div>
<h2><a href="https://leetcode.com/problems/sorting-the-sentence/">1859. Sorting the Sentence</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A <strong style="user-select: auto;">sentence</strong> is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.</p>

<p style="user-select: auto;">A sentence can be <strong style="user-select: auto;">shuffled</strong> by appending the <strong style="user-select: auto;">1-indexed word position</strong> to each word then rearranging the words in the sentence.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, the sentence <code style="user-select: auto;">"This is a sentence"</code> can be shuffled as <code style="user-select: auto;">"sentence4 a3 is2 This1"</code> or <code style="user-select: auto;">"is2 sentence4 This1 a3"</code>.</li>
</ul>

<p style="user-select: auto;">Given a <strong style="user-select: auto;">shuffled sentence</strong> <code style="user-select: auto;">s</code> containing no more than <code style="user-select: auto;">9</code> words, reconstruct and return <em style="user-select: auto;">the original sentence</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "is2 sentence4 This1 a3"
<strong style="user-select: auto;">Output:</strong> "This is a sentence"
<strong style="user-select: auto;">Explanation:</strong> Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "Myself2 Me1 I4 and3"
<strong style="user-select: auto;">Output:</strong> "Me Myself and I"
<strong style="user-select: auto;">Explanation:</strong> Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= s.length &lt;= 200</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of lowercase and uppercase English letters, spaces, and digits from <code style="user-select: auto;">1</code> to <code style="user-select: auto;">9</code>.</li>
	<li style="user-select: auto;">The number of words in <code style="user-select: auto;">s</code> is between <code style="user-select: auto;">1</code> and <code style="user-select: auto;">9</code>.</li>
	<li style="user-select: auto;">The words in <code style="user-select: auto;">s</code> are separated by a single space.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> contains no leading or trailing spaces.</li>
</ul></div>
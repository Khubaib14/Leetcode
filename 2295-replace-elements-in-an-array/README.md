<h2><a href="https://leetcode.com/problems/replace-elements-in-an-array/">2295. Replace Elements in an Array</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given a <strong style="user-select: auto;">0-indexed</strong> array <code style="user-select: auto;">nums</code> that consists of <code style="user-select: auto;">n</code> <strong style="user-select: auto;">distinct</strong> positive integers. Apply <code style="user-select: auto;">m</code> operations to this array, where in the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> operation you replace the number <code style="user-select: auto;">operations[i][0]</code> with <code style="user-select: auto;">operations[i][1]</code>.</p>

<p style="user-select: auto;">It is guaranteed that in the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> operation:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">operations[i][0]</code> <strong style="user-select: auto;">exists</strong> in <code style="user-select: auto;">nums</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">operations[i][1]</code> does <strong style="user-select: auto;">not</strong> exist in <code style="user-select: auto;">nums</code>.</li>
</ul>

<p style="user-select: auto;">Return <em style="user-select: auto;">the array obtained after applying all the operations</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]
<strong style="user-select: auto;">Output:</strong> [3,2,7,1]
<strong style="user-select: auto;">Explanation:</strong> We perform the following operations on nums:
- Replace the number 1 with 3. nums becomes [<u style="user-select: auto;"><strong style="user-select: auto;">3</strong></u>,2,4,6].
- Replace the number 4 with 7. nums becomes [3,2,<u style="user-select: auto;"><strong style="user-select: auto;">7</strong></u>,6].
- Replace the number 6 with 1. nums becomes [3,2,7,<u style="user-select: auto;"><strong style="user-select: auto;">1</strong></u>].
We return the final array [3,2,7,1].
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2], operations = [[1,3],[2,1],[3,2]]
<strong style="user-select: auto;">Output:</strong> [2,1]
<strong style="user-select: auto;">Explanation:</strong> We perform the following operations to nums:
- Replace the number 1 with 3. nums becomes [<u style="user-select: auto;"><strong style="user-select: auto;">3</strong></u>,2].
- Replace the number 2 with 1. nums becomes [3,<u style="user-select: auto;"><strong style="user-select: auto;">1</strong></u>].
- Replace the number 3 with 2. nums becomes [<u style="user-select: auto;"><strong style="user-select: auto;">2</strong></u>,1].
We return the array [2,1].
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == nums.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">m == operations.length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n, m &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;">All the values of <code style="user-select: auto;">nums</code> are <strong style="user-select: auto;">distinct</strong>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">operations[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums[i], operations[i][0], operations[i][1] &lt;= 10<sup style="user-select: auto;">6</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">operations[i][0]</code> will exist in <code style="user-select: auto;">nums</code> when applying the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> operation.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">operations[i][1]</code> will not exist in <code style="user-select: auto;">nums</code> when applying the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> operation.</li>
</ul>
</div>
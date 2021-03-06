<h2><a href="https://leetcode.com/problems/minimum-absolute-difference/">1200. Minimum Absolute Difference</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of <strong style="user-select: auto;">distinct</strong> integers <code style="user-select: auto;">arr</code>, find all pairs of elements with the minimum absolute difference of any two elements.</p>

<p style="user-select: auto;">Return a list of pairs in ascending order(with respect to pairs), each pair <code style="user-select: auto;">[a, b]</code> follows</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">a, b</code> are from <code style="user-select: auto;">arr</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">a &lt; b</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">b - a</code> equals to the minimum absolute difference of any two elements in <code style="user-select: auto;">arr</code></li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [4,2,1,3]
<strong style="user-select: auto;">Output:</strong> [[1,2],[2,3],[3,4]]
<strong style="user-select: auto;">Explanation: </strong>The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [1,3,6,10,15]
<strong style="user-select: auto;">Output:</strong> [[1,3]]
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [3,8,-10,23,19,-4,-14,27]
<strong style="user-select: auto;">Output:</strong> [[-14,-10],[19,23],[23,27]]
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= arr.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">6</sup> &lt;= arr[i] &lt;= 10<sup style="user-select: auto;">6</sup></code></li>
</ul>
</div>
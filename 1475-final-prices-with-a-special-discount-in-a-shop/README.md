<h2><a href="https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/">1475. Final Prices With a Special Discount in a Shop</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the array <code style="user-select: auto;">prices</code> where <code style="user-select: auto;">prices[i]</code> is the price of the <code style="user-select: auto;">ith</code> item in a shop. There is a special discount for items in the shop, if you buy the <code style="user-select: auto;">ith</code> item, then you will receive a discount equivalent to <code style="user-select: auto;">prices[j]</code> where <code style="user-select: auto;">j</code> is the <strong style="user-select: auto;">minimum</strong>&nbsp;index such that <code style="user-select: auto;">j &gt; i</code> and <code style="user-select: auto;">prices[j] &lt;= prices[i]</code>, otherwise, you will not receive any discount at all.</p>

<p style="user-select: auto;"><em style="user-select: auto;">Return an array where the <code style="user-select: auto;">ith</code> element is the final price you will pay for the <code style="user-select: auto;">ith</code> item of the shop considering the special discount.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> prices = [8,4,6,2,3]
<strong style="user-select: auto;">Output:</strong> [4,2,4,2,3]
<strong style="user-select: auto;">Explanation:</strong>&nbsp;
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.&nbsp;
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.&nbsp;
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.&nbsp;
For items 3 and 4 you will not receive any discount at all.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> prices = [1,2,3,4,5]
<strong style="user-select: auto;">Output:</strong> [1,2,3,4,5]
<strong style="user-select: auto;">Explanation:</strong> In this case, for all items, you will not receive any discount at all.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> prices = [10,1,1,6]
<strong style="user-select: auto;">Output:</strong> [9,0,1,6]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= prices.length &lt;= 500</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= prices[i] &lt;= 10^3</code></li>
</ul>
</div>
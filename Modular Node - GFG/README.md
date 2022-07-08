# Modular Node
## Easy
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given a singly linked list and a number <strong style="user-select: auto;">k</strong>, you&nbsp;are required to complete the function <strong style="user-select: auto;">modularNode()&nbsp;</strong>which&nbsp;returns the modular node of the linked list.<br style="user-select: auto;">
A modular node is the last node of the linked list whose<strong style="user-select: auto;"> Index</strong> is divisible by the number <strong style="user-select: auto;">k</strong>, i.e. <strong style="user-select: auto;">i%k==0</strong>.<br style="user-select: auto;">
<strong style="user-select: auto;">Note:</strong> If no such node is available, return&nbsp;<strong style="user-select: auto;">-1</strong>.</span></p>

<p style="user-select: auto;"><span style="font-size: 20px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong><strong style="user-select: auto;"> </strong>LinkedList: 1-&gt;2-&gt;3-&gt;4-&gt;5-&gt;6-&gt;7
&nbsp;      k = 3
<strong style="user-select: auto;">Output: </strong>6
<strong style="user-select: auto;">Explanation:</strong> Node from the last with
index divisible by 3 is 6</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 20px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong><strong style="user-select: auto;"> </strong>LinkedList: 19-&gt;28-&gt;37-&gt;46-&gt;55<strong style="user-select: auto;">
           </strong>k = 2<strong style="user-select: auto;">
Output: </strong>46<strong style="user-select: auto;">
Explanation:</strong> Node from the last with
index divisible by 2 is 46</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Your Task:</span></strong></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">You don't need to read input or print anything. Complete the function modularNode() which takes the head Node and integer k&nbsp;as input parameters and returns the modular Node, if exists,<strong style="user-select: auto;"> -1 otherwise</strong>.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 &lt;= T &lt;= 100<br style="user-select: auto;">
1 &lt;= N &lt;= 500</span></p>
 <p style="user-select: auto;"></p>
            </div>
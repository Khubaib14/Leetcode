# Queue using stack
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Implement a Queue&nbsp;using two stack</span><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">&nbsp;s1</strong>&nbsp;and<strong style="user-select: auto;">&nbsp;s2</strong>.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>enqueue(2)
enqueue(3)
dequeue()
enqueue(4)
dequeue()<strong style="user-select: auto;">
Output: </strong>2 3
<strong style="user-select: auto;">Explanation:
</strong>enqueue(2)&nbsp;the queue&nbsp;will be {2}
enqueue(3)&nbsp;the queue&nbsp;will be {3 2}
dequeue() the poped element will be 2&nbsp;
the stack&nbsp;will be {3}
enqueue(4)&nbsp;the stack&nbsp;will be {4 3}
dequeue() the poped element will be 3. &nbsp;
</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:
</strong>enqueue(2)
dequeue()
dequeue()<strong style="user-select: auto;">
Output: </strong>2 -1</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong></span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Since this is a function problem, you don't need to take inputs. You are required to complete the two methods&nbsp;<strong style="user-select: auto;">enqueue</strong><strong style="user-select: auto;">()</strong>&nbsp;which takes&nbsp;an integer <strong style="user-select: auto;">'x'</strong>&nbsp;as input&nbsp;denoting the element to be pushed into the queue&nbsp;and <strong style="user-select: auto;">dequeue</strong><strong style="user-select: auto;">()</strong>&nbsp;which returns the&nbsp;integer&nbsp;poped out from the queue.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:&nbsp;</strong>O(1) for&nbsp;<strong style="user-select: auto;">enqueue</strong><strong style="user-select: auto;">()&nbsp;</strong>and O(n) for <strong style="user-select: auto;">dequeue</strong><strong style="user-select: auto;">()</strong><br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:&nbsp;</strong>O(1) for both&nbsp;<strong style="user-select: auto;">enqueue</strong><strong style="user-select: auto;">()&nbsp;</strong>and <strong style="user-select: auto;">dequeue</strong><strong style="user-select: auto;">()</strong></span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 &lt;=<strong style="user-select: auto;">&nbsp;</strong>Number of queries&nbsp;&lt;= 100<br style="user-select: auto;">
1 &lt;= values of the stack&nbsp;&lt;= 100</span></p>
 <p style="user-select: auto;"></p>
            </div>
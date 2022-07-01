# Stack using two queues
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Implement a Stack&nbsp;using two queues<strong style="user-select: auto;">&nbsp;q1</strong>&nbsp;and<strong style="user-select: auto;">&nbsp;q2</strong>.</span></p>

<p style="user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Example 1:</span></strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Input:
</span></strong><span style="font-size: 18px; user-select: auto;">push(2)
push(3)
pop()
push(4)
pop()</span><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">
Output: </span></strong><span style="font-size: 18px; user-select: auto;">3 4
</span><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Explanation:
</span></strong><span style="font-size: 18px; user-select: auto;">push(2)&nbsp;the stack&nbsp;will be {2}
push(3)&nbsp;the stack&nbsp;will be {2 3}
pop()   poped element will be 3&nbsp;the 
&nbsp;       stack&nbsp;will be {2}
push(4)&nbsp;the stack&nbsp;will be {2 4}
pop() &nbsp; poped element will be 4 &nbsp;</span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Example 2:</span></strong></p>

<pre style="position: relative; user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Input:
</span></strong><span style="font-size: 18px; user-select: auto;">push(2)
pop()
pop()
push(3)</span><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">
Output: </span></strong><span style="font-size: 18px; user-select: auto;">2 -1</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Your Task:</span></strong></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Since this is a function problem, you don't need to take inputs. You are required to complete the two methods&nbsp;<strong style="user-select: auto;">push()</strong>&nbsp;which takes&nbsp;an integer <strong style="user-select: auto;">'x'</strong>&nbsp;as input&nbsp;denoting the element to be pushed into the stack and&nbsp;<strong style="user-select: auto;">pop()</strong>&nbsp;which returns the&nbsp;integer&nbsp;poped out from the stack(<strong style="user-select: auto;">-1</strong>&nbsp;if the stack&nbsp;is empty).</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:&nbsp;</strong>O(1) for&nbsp;<strong style="user-select: auto;">push()&nbsp;</strong>and O(N) for&nbsp;<strong style="user-select: auto;">pop()&nbsp;</strong>(or vice-versa).<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:&nbsp;</strong>O(1) for both&nbsp;<strong style="user-select: auto;">push()&nbsp;</strong>and&nbsp;<strong style="user-select: auto;">pop()</strong>.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 &lt;=<strong style="user-select: auto;">&nbsp;</strong>Number of queries&nbsp;&lt;= 100<br style="user-select: auto;">
1 &lt;= values of the stack&nbsp;&lt;= 100</span></p>
 <p style="user-select: auto;"></p>
            </div>
# Get min at pop
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><em style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Now, we'll try to solve a famous stack problem. </span></em><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;">You are given an array <strong style="user-select: auto;">A</strong> of size <strong style="user-select: auto;">N</strong>. You need to first push the elements of the array into a stack and then print minimum in the stack at each pop.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input</strong>:
N = 5
A = {1 2 3 4 5}
<strong style="user-select: auto;">Output</strong>: 
1 1 1 1 1
<strong style="user-select: auto;">Explanation</strong>: 
After pushing elements to the stack, 
the stack will be "top -&gt; 5, 4, 3, 2, 1". 
Now, start popping elements from the stack
popping&nbsp;5: min in&nbsp;the stack is&nbsp;1.popped 5
popping&nbsp;4: min in the stack is 1. popped 4
popping&nbsp;3: min in the stack is&nbsp;1. popped 3
popping 2: min in the stack is 1. popped 2
popping 1: min in the stack is 1. popped 1
</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input</strong>: 
N = 7
A = {1 6 43 1 2 0 5}
<strong style="user-select: auto;">Output</strong>: 
0 0 1 1 1 1 1
<strong style="user-select: auto;">Explanation</strong>: 
After pushing the elements to the stack, 
the stack will be 5-&gt;0-&gt;2-&gt;1-&gt;43-&gt;6-&gt;1. 
Now, poping the elements from the stack:
popping 5: min in the stack is 0. popped 5
popping 0: min in the stack is 0. popped 0
popping 2: min in the stack is 1. popped 2
popping 1: min in the stack is 1. popped 1
popping 43: min in the stack is 1. 
&nbsp;           popped 43
popping 6: min in the stack is 1. popped 6
popping 1: min in the stack is 1. popped 1.
</span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
Since this is a function problem, you don't need to take any input. Just complete the provided functions <strong style="user-select: auto;">_push()</strong> and <strong style="user-select: auto;">_getMinAtPop().&nbsp;</strong>The _push() function takes an array as parameter, you need to push all elements of this array onto a stack and return the stack. The _getMinAtPop() accepts a stack as a parameter which is returned by _push() function and prints minimum in the stack at each pop separated by spaces.</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:&nbsp;</strong>O(N).<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:&nbsp;</strong>O(N).</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<strong style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Constraints:</span></strong><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;">1 &lt;= A<sub style="user-select: auto;">i</sub> &lt;= 10<sup style="user-select: auto;">7</sup></span></p>
 <p style="user-select: auto;"></p>
            </div>
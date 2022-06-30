# Pairwise Consecutive Elements
## Easy
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given a stack of integers of size <strong style="user-select: auto;">N</strong>, your task is to complete the&nbsp;function <strong style="user-select: auto;">pairWiseConsecutive(),</strong> that checks whether numbers in the stack are pairwise consecutive or not. The pairs can be increasing or decreasing, and if the stack has an odd number of elements, the element at the top is left out of a pair. The function should retain the original stack content.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Only following standard operations are allowed on </span><span style="font-size: 18px; user-select: auto;">stack</span><span style="font-size: 18px; user-select: auto;">.</span></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">push(X): Enter </span><span style="font-size: 18px; user-select: auto;">a element</span><span style="font-size: 18px; user-select: auto;"> X on top of </span><span style="font-size: 18px; user-select: auto;">stack</span><span style="font-size: 18px; user-select: auto;">.</span></li>
	<li style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">pop(): Removes top element of the stack.</span></li>
	<li style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">empty(): To check if stack is empty.</span></li>
</ul>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input Format:</strong><br style="user-select: auto;">
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input. The first line contains n denoting the number of elements to be inserted into the stack. The second line contains the elements to be inserted into the stack.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Output Format:</strong><br style="user-select: auto;">
For each</span><span style="font-size: 18px; user-select: auto;"> testcase, in a new line, print </span><span style="font-size: 18px; user-select: auto;">"<strong style="user-select: auto;">Yes</strong>"(without quote) if the elements of the stack </span><span style="font-size: 18px; user-select: auto;">is</span><span style="font-size: 18px; user-select: auto;"> pairwise consecutive, else print&nbsp;"<strong style="user-select: auto;">No</strong>".</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
This is a function problem. You only need to complete the function <strong style="user-select: auto;">pairWiseConsecutive </strong>that takes a stack as an <strong style="user-select: auto;">argument </strong>and returns <strong style="user-select: auto;">true </strong>if the stack is found to be pairwise consecutive, else it returns <strong style="user-select: auto;">false</strong>. The printing is done by the <strong style="user-select: auto;">driver </strong>code.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 &lt; =T &lt;= 100<br style="user-select: auto;">
1 &lt; =N &lt;= 10<sup style="user-select: auto;">3</sup></span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example:<br style="user-select: auto;">
Input:</strong><br style="user-select: auto;">
2<br style="user-select: auto;">
6<br style="user-select: auto;">
1 2 3 4 5 6<br style="user-select: auto;">
5<br style="user-select: auto;">
1 5 3 9 7<br style="user-select: auto;">
<strong style="user-select: auto;">Output:</strong><br style="user-select: auto;">
Yes</span><br style="user-select: auto;">
<span style="font-size: 20px; user-select: auto;">No</span></p>

<p style="user-select: auto;"><span style="font-size: 20px; user-select: auto;"><strong style="user-select: auto;">Explanation:</strong><br style="user-select: auto;">
<strong style="user-select: auto;">Testcase1: </strong>The number of elements are even and they are pairwise consecutive so we print Yes.<br style="user-select: auto;">
<strong style="user-select: auto;">Testcase2: </strong>The number of elements are odd so we remove the top element and check for pairwise consecutive. It is not so we print No.</span></p>
 <p style="user-select: auto;"></p>
            </div>
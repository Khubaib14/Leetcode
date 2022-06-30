# Stack Operations
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><em style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">This Java module deals with Stacks, Queues, and ArrayLists. We'll perform various operations on them.</span></em></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given a <strong style="user-select: auto;">stack </strong>of <strong style="user-select: auto;">integers </strong>and <strong style="user-select: auto;">Q</strong> queries. The task is to perform operation on stack according to the query.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Note</strong><span style="background-color: transparent; color: rgb(0, 0, 0); font-family: arial; --darkreader-inline-bgcolor:transparent; --darkreader-inline-color:#e8e6e3; user-select: auto;" data-darkreader-inline-bgcolor="" data-darkreader-inline-color="">: use </span><a href="https://www.geeksforgeeks.org/stack-push-method-in-java/" style="text-decoration: none; user-select: auto;" target="_blank"><u style="user-select: auto;">push()</u></a><span style="background-color: transparent; color: rgb(0, 0, 0); font-family: arial; --darkreader-inline-bgcolor:transparent; --darkreader-inline-color:#e8e6e3; user-select: auto;" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""> to add element in the stack, </span><a href="https://www.geeksforgeeks.org/stack-peek-method-in-java/" style="text-decoration: none; user-select: auto;" target="_blank"><u style="user-select: auto;">peek()</u></a><span style="background-color: transparent; color: rgb(0, 0, 0); font-family: arial; --darkreader-inline-bgcolor:transparent; --darkreader-inline-color:#e8e6e3; user-select: auto;" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""> to get topmost element without removal, </span><a href="https://www.geeksforgeeks.org/stack-pop-method-in-java/" style="text-decoration: none; user-select: auto;" target="_blank"><u style="user-select: auto;">pop()</u></a><span style="background-color: transparent; color: rgb(0, 0, 0); font-family: arial; --darkreader-inline-bgcolor:transparent; --darkreader-inline-color:#e8e6e3; user-select: auto;" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""> gives topmost element with removal, </span><a href="https://www.geeksforgeeks.org/stack-search-method-in-java/" style="text-decoration: none; user-select: auto;" target="_blank"><u style="user-select: auto;">search()</u></a><span style="background-color: transparent; color: rgb(0, 0, 0); font-family: arial; --darkreader-inline-bgcolor:transparent; --darkreader-inline-color:#e8e6e3; user-select: auto;" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""> to return position if found else <strong style="user-select: auto;">-1</strong>.</span></span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input Format:</strong><br style="user-select: auto;">
First line of input contains nubmer of testcases <strong style="user-select: auto;">T</strong>. For each testcase, first line of input contains Q, number of queries. Next line contains Q queries seperated by space. Queries are as:</span></p>

<ol style="user-select: auto;">
	<li dir="ltr" style="user-select: auto;">
	<p dir="ltr" style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><span style="background-color: transparent; color: rgb(0, 0, 0); font-family: arial; --darkreader-inline-bgcolor:transparent; --darkreader-inline-color:#e8e6e3; user-select: auto;" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><strong style="user-select: auto;">i x :</strong> (<strong style="user-select: auto;">adds </strong>element x in the stack)</span>.</span></p>
	</li>
	<li dir="ltr" style="user-select: auto;">
	<p dir="ltr" style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><span style="background-color: transparent; color: rgb(0, 0, 0); font-family: arial; --darkreader-inline-bgcolor:transparent; --darkreader-inline-color:#e8e6e3; user-select: auto;" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><strong style="user-select: auto;">r :</strong> (<strong style="user-select: auto;">returns </strong>and <strong style="user-select: auto;">removes </strong>the topmost element from the stack).</span></span></p>
	</li>
	<li dir="ltr" style="user-select: auto;">
	<p dir="ltr" style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><span style="background-color: transparent; color: rgb(0, 0, 0); font-family: arial; --darkreader-inline-bgcolor:transparent; --darkreader-inline-color:#e8e6e3; user-select: auto;" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><strong style="user-select: auto;">h :</strong> </span>Prints the topmost element.</span></p>
	</li>
	<li dir="ltr" style="user-select: auto;">
	<p dir="ltr" style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><span style="background-color: transparent; color: rgb(0, 0, 0); font-family: arial; --darkreader-inline-bgcolor:transparent; --darkreader-inline-color:#e8e6e3; user-select: auto;" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><strong style="user-select: auto;">f y :</strong> (check if the <strong style="user-select: auto;">element </strong>y is <strong style="user-select: auto;">present or not </strong>in the stack).</span> Print "<strong style="user-select: auto;">Yes</strong>" if present, else "<strong style="user-select: auto;">No</strong>".</span></p>
	</li>
</ol>

<p dir="ltr" style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Output Format:</strong><br style="user-select: auto;">
For each testcase, perform Q queries and print the output wherever required.</span></p>

<p dir="ltr" style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
Your task is to complete functions <strong style="user-select: auto;">insert()</strong>, <strong style="user-select: auto;">remove()</strong>, <strong style="user-select: auto;">headOf_Stack()</strong> and <strong style="user-select: auto;">find()</strong>, to insert, remove returning top element and findiing the elment in stack respectively.</span></p>

<p dir="ltr" style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 &lt;= T &lt;= 100<br style="user-select: auto;">
1 &lt;= Q &lt;= 10<sup style="user-select: auto;">3</sup></span></p>

<p dir="ltr" style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example:<br style="user-select: auto;">
Input:</strong><br style="user-select: auto;">
2<br style="user-select: auto;">
6<br style="user-select: auto;">
i 2 i 4 i 3 i 5 h f 8<br style="user-select: auto;">
4<br style="user-select: auto;">
i 3 i 4 r f 3</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Output:</strong><br style="user-select: auto;">
5<br style="user-select: auto;">
No<br style="user-select: auto;">
Yes</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Explanation:<br style="user-select: auto;">
Testcase 1:</strong> Inserting 2, 4, 3, and 5 onto the stack. Returning top element which is 5. Finding 8 will give No, as 8 is not in the stack.</span></p>
 <p style="user-select: auto;"></p>
            </div>
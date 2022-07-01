# Save Gotham!
## Medium 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Gotham has been attacked by Joker . Bruce Wayne has deployed an automatic machine gun at each tower of Gotham.<br style="user-select: auto;">
All the towers in Gotham are in a straight line.<br style="user-select: auto;">
You are given no of towers 'n' followed by the height of 'n' towers.<br style="user-select: auto;">
For every tower(p), find the height of the closest tower (towards the right), greater than the height of the tower(p).<br style="user-select: auto;">
Now, the Print sum of all such heights (mod 1000000001).</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Note:</strong> If for a tower(k), no such tower exists then take its height as 0.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">â€‹Input :</strong> arr[]= {112, 133, 161, 311, 122, 
                    512, 1212, 0, 19212}
<strong style="user-select: auto;">Output :</strong> 41265
<strong style="user-select: auto;">Explanation:</strong>
nextgreater(112) : 133
nextgreater(133) : 161
nextgreater(161) : 311
nextgreater(311) : 512
nextgreater(122) : 512
nextgreater(512) : 1212
nextgreater(1212) : 19212
nextgreater(0) : 19212
nextgreater(19212) : 0
add = 133+161+311+512+512+1212+19212+19212+0 
add = 41265.</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">â€‹Example 2:</strong></span></p>

<pre style="position: relative; user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input :</strong> arr[] = {5, 9, 7, 6} <strong style="user-select: auto;">
Output :</strong>  9

</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper" style="user-select: auto;"></div></pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <strong style="user-select: auto;">save_gotham()</strong> that takes an array <strong style="user-select: auto;">(arr)</strong>, sizeOfArray <strong style="user-select: auto;">(n)</strong>, and return the sum of next greater element of every element. The driver code takes care of the printing.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong>&nbsp;O(N).<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong>&nbsp;O(N).</span></p>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 ≤ N ≤ 10<sup style="user-select: auto;">5</sup><br style="user-select: auto;">
0 ≤ A[i] ≤ 10<sup style="user-select: auto;">4</sup></span></p>
 <p style="user-select: auto;"></p>
            </div>
# Permutation with Spaces
## Easy 
<div class="problem-statement">
                <p></p><p><span style="font-size:18px">Given a string you need to print all possible strings that can be made by placing spaces (zero or one) in between them. The output should be printed in <strong>sorted</strong> <strong>increasing</strong> order of strings</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre style="margin-bottom: 0px;"><span style="font-size:18px"><strong>Input</strong>:
S = "ABC"
<strong>Output: </strong>(A B C)(A BC)(AB C)(ABC)
<strong>Explanation</strong>:
ABC
AB C
A BC
A B C
These are the possible combination of "ABC".</span></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/permutation-with-spaces3627/1&amp;title=Permutation%20with%20Spaces%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0AS%20%3D%20%22ABC%22%0AOutput%3A%20(A%20B%20C)(A%20BC)(AB%20C)(ABC)%0AExplanation%3A%0AABC%0AAB%20C%0AA%20BC%0AA%20B%20C%0AThese%20are%20the%20possible%20combination%20of%20%22ABC%22." class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre style="margin-bottom: 0px;"><span style="font-size:18px"><strong>Input:</strong>
S = "AB"
<strong>Output: </strong>(A B)(AB)
</span></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/permutation-with-spaces3627/1&amp;title=Permutation%20with%20Spaces%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0AS%20%3D%20%22AB%22%0AOutput%3A%20(A%20B)(AB)%0A" class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>permutation()</strong>&nbsp;which takes the string S as input parameters and returns the <strong>sorted array&nbsp;</strong>of the string denoting the different permutation <strong>(DON'T ADD '(' and ')' it will be handled by the driver code only)</strong>.<br>
<br>
<strong>Expected Time Complexity:</strong> O(2^n)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>CONSTRAINTS:</strong><br>
1 &lt; |S| &lt; 10<br>
S only contains <strong>lowercase and Uppercase English</strong> letters.</span></p>
 <p></p>
            </div>
# First negative integer in every window of size k
## Easy 
<div class="problem-statement">
                <p></p><p><span style="font-size:18px">Given an array <strong>A[] </strong>of size <strong>N</strong> and a positive integer <strong>K</strong>, find the first negative integer for each and every window(contiguous subarray) of size <strong>K</strong>.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre style="margin-bottom: 0px;"><span style="font-size:18px"><strong>Input : 
</strong>N = 5
A[] = {-8, 2, 3, -6, 10}
K = 2
<strong>Output : </strong>
-8 0 -6 -6
<strong>Explanation :</strong>
First negative integer for each window of size k
<strong>{-8, 2}</strong> = -8
<strong>{2, 3}</strong> = 0 (does not contain a negative integer)
<strong>{3, -6}</strong> = -6
<strong>{-6, 10}</strong> = -6</span></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1&amp;title=First%20negative%20integer%20in%20every%20window%20of%20size%20k%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%20%3A%20%0AN%20%3D%205%0AA%5B%5D%20%3D%20%7B-8%2C%202%2C%203%2C%20-6%2C%2010%7D%0AK%20%3D%202%0AOutput%20%3A%20%0A-8%200%20-6%20-6%0AExplanation%20%3A%0AFirst%20negative%20integer%20for%20each%20window%20of%20size%20k%0A%7B-8%2C%202%7D%20%3D%20-8%0A%7B2%2C%203%7D%20%3D%200%20(does%20not%20contain%20a%20negative%20integer)%0A%7B3%2C%20-6%7D%20%3D%20-6%0A%7B-6%2C%2010%7D%20%3D%20-6" class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<div>&nbsp;</div>

<div><span style="font-size:18px"><strong>Example 2:</strong></span></div>

<pre style="margin-bottom: 0px;"><span style="font-size:18px"><strong>Input : </strong>
N = 8
A[] = {12, -1, -7, 8, -15, 30, 16, 28}
K = 3
<strong>Output :</strong>
-1 -1 -7 -15 -15 0 </span></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1&amp;title=First%20negative%20integer%20in%20every%20window%20of%20size%20k%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%20%3A%20%0AN%20%3D%208%0AA%5B%5D%20%3D%20%7B12%2C%20-1%2C%20-7%2C%208%2C%20-15%2C%2030%2C%2016%2C%2028%7D%0AK%20%3D%203%0AOutput%20%3A%0A-1%20-1%20-7%20-15%20-15%200%20" class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>printFirstNegativeInteger()</strong>&nbsp;which takes the array <strong>A[]</strong>, its size <strong>N </strong>and an integer <strong>K </strong>as inputs and returns the first negative number in every window of size K&nbsp;starting from the first till the end. If a window does not contain a negative integer , then return 0 for that window.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N)<br>
<strong>Expected Auxiliary Space:</strong> O(K)<br>
<br>
<strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>5</sup><br>
-10<sup>5</sup> &lt;= A[i] &lt;= 10<sup>5</sup><br>
1 &lt;= K &lt;= N</span></p>
 <p></p>
            </div>
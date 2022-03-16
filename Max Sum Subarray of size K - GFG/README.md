# Max Sum Subarray of size K
## Easy
<div class="problem-statement">
                <p></p><p><span style="font-size:18px">Given an array of integers Arr of size <strong>N</strong> and a number <strong>K</strong>. Return&nbsp;the maximum sum of a subarray of size K.</span></p>

<p>&nbsp;</p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre style="margin-bottom: 0px;"><strong><span style="font-size:18px">Input:</span></strong>
<span style="font-size:18px">N = 4, K = 2
Arr = [100, 200, 300, 400]</span>
<strong><span style="font-size:18px">Output:</span></strong>
<span style="font-size:18px">700</span>
<strong><span style="font-size:18px">Explanation:</span></strong>
<span style="font-size:18px">Arr<sub>3 </sub> + Arr<sub>4</sub> =700,</span>
<span style="font-size:18px">which is maximum.</span></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1&amp;title=Max%20Sum%20Subarray%20of%20size%20K%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0AN%20%3D%204%2C%20K%20%3D%202%0AArr%20%3D%20%5B100%2C%20200%2C%20300%2C%20400%5D%0AOutput%3A%0A700%0AExplanation%3A%0AArr3%20%20%2B%20Arr4%20%3D700%2C%0Awhich%20is%20maximum." class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p>&nbsp;</p>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre style="margin-bottom: 0px;"><strong><span style="font-size:18px">Input:</span></strong>
<span style="font-size:18px">N = 4, K = 4</span>
<span style="font-size:18px">Arr = [100, 200, 300, 400]</span>
<strong><span style="font-size:18px">Output:</span></strong>
<span style="font-size:18px">1000</span>
<strong><span style="font-size:18px">Explanation:</span></strong>
<span style="font-size:18px">Arr<sub>1</sub> + Arr<sub>2</sub> + Arr<sub>3 </sub> 
+ Arr<sub>4</sub> =1000,</span>
<span style="font-size:18px">which is maximum.</span></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1&amp;title=Max%20Sum%20Subarray%20of%20size%20K%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0AN%20%3D%204%2C%20K%20%3D%204%0AArr%20%3D%20%5B100%2C%20200%2C%20300%2C%20400%5D%0AOutput%3A%0A1000%0AExplanation%3A%0AArr1%20%2B%20Arr2%20%2B%20Arr3%20%20%0A%2B%20Arr4%20%3D1000%2C%0Awhich%20is%20maximum." class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p>&nbsp;</p>

<p><strong><span style="font-size:18px">Your Task:</span></strong></p>

<p><span style="font-size:18px">You don't need to read input or print anything. Your task is to complete the function maximumSumSubarray() which takes the integer k, vector Arr with size N,&nbsp;containing the elements of the array and returns the&nbsp;maximum sum of a subarray of size K.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span><br>
&nbsp;</p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1&lt;=N&lt;=10<sup>5</sup><br>
1&lt;=K&lt;=N</span><br>
&nbsp;</p>
 <p></p>
            </div>
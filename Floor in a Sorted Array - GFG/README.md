# Floor in a Sorted Array
## Easy 
<div class="problem-statement">
                <p></p><p><span style="font-size:18px">Given a sorted array <strong>arr</strong>[] of size <strong>N</strong> without duplicates, and given a value <strong>x</strong>. Floor of x is defined as the largest element <strong>K</strong> in arr[] such that K is smaller than or equal to x.&nbsp;Find the index of K(0-based indexing).</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre style="margin-bottom: 0px;"><span style="font-size:18px"><strong>Input:
</strong>N = 7, x = 0 
arr[] = {1,2,8,10,11,12,19}
<strong>Output: </strong>-1<strong>
Explanation: </strong>No element less 
than 0 is found. So output 
is "<strong>-1</strong>".</span></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background: rgb(15, 37, 51); padding: 5px; border-radius: 0px 0px 5px 5px; display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1&amp;title=Floor%20in%20a%20Sorted%20Array%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0AN%20%3D%207%2C%20x%20%3D%200%20%0Aarr%5B%5D%20%3D%20%7B1%2C2%2C8%2C10%2C11%2C12%2C19%7D%0AOutput%3A%20-1%0AExplanation%3A%20No%20element%20less%20%0Athan%200%20is%20found.%20So%20output%20%0Ais%20%22-1%22." class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre style="margin-bottom: 0px;"><span style="font-size:18px"><strong>Input:
</strong>N = 7, x = 5 
arr[] = {1,2,8,10,11,12,19}
<strong>Output: </strong>1<strong>
Explanation: </strong>Largest Number less than 5 is
<strong>2 (i.e K = 2)</strong>, whose index is <strong>1</strong>(0-based 
indexing).</span>
</pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1&amp;title=Floor%20in%20a%20Sorted%20Array%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0AN%20%3D%207%2C%20x%20%3D%205%20%0Aarr%5B%5D%20%3D%20%7B1%2C2%2C8%2C10%2C11%2C12%2C19%7D%0AOutput%3A%201%0AExplanation%3A%20Largest%20Number%20less%20than%205%20is%0A2%20(i.e%20K%20%3D%202)%2C%20whose%20index%20is%201(0-based%20%0Aindexing).%0A" class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p><span style="font-size:18px"><strong>Your&nbsp;Task:</strong><br>
The task is to complete the function <strong>findFloor</strong>() which returns an&nbsp;integer denoting the index value of K&nbsp;or return <strong>-1</strong> if there isn't any such number.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(log N).<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1).</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>7</sup><br>
1 ≤ arr[i] ≤ 10<sup>18</sup><br>
0 ≤ X&nbsp;≤<sup> </sup>arr[n-1]</span></p>
 <p></p>
            </div>
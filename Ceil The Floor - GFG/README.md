# Ceil The Floor
## Easy
<div class="problem-statement">
                <p></p><p><span style="font-size:18px">Given an unsorted array <strong>Arr[]</strong>&nbsp;of <strong>N</strong> integers and an integer&nbsp;<strong>X</strong>, find floor and ceiling of <strong>X</strong>&nbsp;in <strong>Arr[0..N-1]</strong>.</span></p>

<p><span style="font-size:18px"><strong>Floor</strong>&nbsp;of <strong>X</strong> is the largest element which is smaller than or equal to <strong>X</strong>. Floor of <strong>X</strong>&nbsp;doesn’t exist if <strong>X</strong>&nbsp;is smaller than smallest element of <strong>Arr[]</strong>.</span></p>

<p><span style="font-size:18px"><strong>Ceil</strong>&nbsp;of <strong>X</strong>&nbsp;is the smallest element which is greater than or equal to <strong>X</strong>. Ceil of <strong>X</strong>&nbsp;doesn’t exist if <strong>X</strong> is greater than greatest element of <strong>Arr[]</strong>.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre style="margin-bottom: 0px;"><span style="font-size:18px"><strong>Input:
</strong>N = 8, X = 7
Arr[] = {5, 6, 8, 9, 6, 5, 5, 6}
<strong>Output:</strong> 6 8
<strong>Explanation:
</strong>Floor of 7 is 6 and ceil of 7 
is 8.
</span></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/ceil-the-floor2802/1&amp;title=Ceil%20The%20Floor%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0AN%20%3D%208%2C%20X%20%3D%207%0AArr%5B%5D%20%3D%20%7B5%2C%206%2C%208%2C%209%2C%206%2C%205%2C%205%2C%206%7D%0AOutput%3A%206%208%0AExplanation%3A%0AFloor%20of%207%20is%206%20and%20ceil%20of%207%20%0Ais%208.%0A" class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre style="margin-bottom: 0px;"><span style="font-size:18px"><strong>Input:
</strong>N = 8, X = 10
Arr[] = {5, 6, 8, 9, 6, 5, 5, 6}
<strong>Output:</strong> 9 -1
<strong>Explanation:
</strong>Floor of 10 is 9 but ceil of 10 is not 
possible.
</span></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/ceil-the-floor2802/1&amp;title=Ceil%20The%20Floor%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0AN%20%3D%208%2C%20X%20%3D%2010%0AArr%5B%5D%20%3D%20%7B5%2C%206%2C%208%2C%209%2C%206%2C%205%2C%205%2C%206%7D%0AOutput%3A%209%20-1%0AExplanation%3A%0AFloor%20of%2010%20is%209%20but%20ceil%20of%2010%20is%20not%20%0Apossible.%0A" class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>getFloorAndCeil()</strong>&nbsp;which takes the array of integers&nbsp;<strong>arr, n</strong>&nbsp;and&nbsp;<strong>x&nbsp;</strong>as parameters and returns a pair&nbsp;of integers denoting the answer. Return <strong>-1</strong> if floor or ceil is not present.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints :</strong><br>
1 ≤ N&nbsp;≤ 10<sup>5</sup><br>
1 ≤ Arr[i], X ≤ 10<sup>6</sup></span></p>

<p>&nbsp;</p>
 <p></p>
            </div>
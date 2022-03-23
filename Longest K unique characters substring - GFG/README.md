# Longest K unique characters substring
## Easy 
<div class="problem-statement">
                <p></p><p><span style="font-size:18px">Given a string you need to print the size of the longest possible substring that has exactly K&nbsp;unique characters. If there is no possible substring then print -1.</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre style="margin-bottom: 0px;"><span style="font-size:18px"><strong>Input:</strong>
S = "aabacbebebe</span><span style="font-size:18px">", K = 3
<strong>Output:</strong> 7
<strong>Explanation</strong>: "cbebebe" is the longest 
substring with K distinct characters.
</span></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background: rgb(15, 37, 51); padding: 5px; border-radius: 0px 0px 5px 5px; display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1&amp;title=Longest%20K%20unique%20characters%20substring%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0AS%20%3D%20%22aabacbebebe%22%2C%20K%20%3D%203%0AOutput%3A%207%0AExplanation%3A%20%22cbebebe%22%20is%20the%20longest%20%0Asubstring%20with%20K%20distinct%20characters.%0A" class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre style="margin-bottom: 0px;"><span style="font-size:18px"><strong>Input</strong>: 
S = "aaaa", K = 2
<strong>Output:</strong> -1
<strong>Explanation</strong>: There's no substring with K
distinct characters.
</span></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1&amp;title=Longest%20K%20unique%20characters%20substring%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%20%0AS%20%3D%20%22aaaa%22%2C%20K%20%3D%202%0AOutput%3A%20-1%0AExplanation%3A%20There%2527s%20no%20substring%20with%20K%0Adistinct%20characters.%0A" class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>longestKSubstr()&nbsp;</strong>which takes the string S and an integer K as input and returns the length of the longest substring with exactly K&nbsp;distinct characters. If there is no substring with exactly K distinct characters then return -1.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(|S|).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(1).</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ |S| ≤ 10<sup>5</sup><br>
1 ≤ K ≤ 10<sup>5</sup></span></p>
 <p></p>
            </div>
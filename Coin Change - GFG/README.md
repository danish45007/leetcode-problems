# Coin Change
## Medium 
<div class="problem-statement">
                <p></p><p><span style="font-size:18px">Given a value N, find the number of ways to make change for N cents, if we have infinite supply of each of S = { S<sub>1</sub>, S<sub>2</sub>, .. , S<sub>M&nbsp;</sub>} valued coins. </span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre style="margin-bottom: 0px;"><span style="font-size:18px"><strong>Input:</strong>
n = 4 , m = 3
S[] = {1,2,3}
<strong>Output:</strong> 4
<strong>Explanation</strong>: Four Possible ways are:
{1,1,1,1},{1,1,2},{2,2},{1,3}.</span>
</pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/coin-change2448/1&amp;title=Coin%20Change%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0An%20%3D%204%20%2C%20m%20%3D%203%0AS%5B%5D%20%3D%20%7B1%2C2%2C3%7D%0AOutput%3A%204%0AExplanation%3A%20Four%20Possible%20ways%20are%3A%0A%7B1%2C1%2C1%2C1%7D%2C%7B1%2C1%2C2%7D%2C%7B2%2C2%7D%2C%7B1%2C3%7D.%0A" class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre style="margin-bottom: 0px;"><span style="font-size:18px"><strong>Input</strong>:
n = 10 , m = 4
S[] ={2,5,3,6}
<strong>Output:</strong> 5
<strong>Explanation</strong>: Five Possible ways are:
{2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} 
and {5,5}.
</span></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/coin-change2448/1&amp;title=Coin%20Change%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0An%20%3D%2010%20%2C%20m%20%3D%204%0AS%5B%5D%20%3D%7B2%2C5%2C3%2C6%7D%0AOutput%3A%205%0AExplanation%3A%20Five%20Possible%20ways%20are%3A%0A%7B2%2C2%2C2%2C2%2C2%7D%2C%20%7B2%2C2%2C3%2C3%7D%2C%20%7B2%2C2%2C6%7D%2C%20%7B2%2C3%2C5%7D%20%0Aand%20%7B5%2C5%7D.%0A" class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>count()&nbsp;</strong>which accepts an array <strong>S[] </strong>its size <strong>m </strong>and <strong>n</strong>&nbsp;as input parameter and returns the number of ways to make change for N cents.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(m*n).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(n). </span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= n,m &lt;= 10<sup>3</sup></span></p>
 <p></p>
            </div>
# Count Occurences of Anagrams
## Medium 
<div class="problem-statement">
                <p></p><p><span style="font-size:18px">Given a word <strong>pat</strong>&nbsp;and a text <strong>txt</strong>. Return the count of the occurences of anagrams of the word in the text.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre style="margin-bottom: 0px;"><span style="font-size:18px"><strong>Input:
</strong>txt = forxxorfxdofr
pat = for
<strong>Output:</strong> 3
<strong>Explanation:</strong> <strong>for, orf</strong> and <strong>ofr </strong>appears
in the <strong>txt, </strong>hence answer is 3.
</span></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background: rgb(15, 37, 51); padding: 5px; border-radius: 0px 0px 5px 5px; display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1&amp;title=Count%20Occurences%20of%20Anagrams%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0Atxt%20%3D%20forxxorfxdofr%0Apat%20%3D%20for%0AOutput%3A%203%0AExplanation%3A%20for%2C%20orf%20and%20ofr%20appears%0Ain%20the%20txt%2C%20hence%20answer%20is%203.%0A" class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre style="margin-bottom: 0px;"><span style="font-size:18px"><strong>Input:
</strong>txt = aabaabaa
pat = aaba
<strong>Output:</strong> 4
<strong>Explanation:</strong>&nbsp;<strong>aaba</strong> is present 4 times
in <strong>txt</strong>.
</span></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:10px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1&amp;title=Count%20Occurences%20of%20Anagrams%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0Atxt%20%3D%20aabaabaa%0Apat%20%3D%20aaba%0AOutput%3A%204%0AExplanation%3A%C2%A0aaba%20is%20present%204%20times%0Ain%20txt.%0A" class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
Complete the function <strong>search()</strong>&nbsp;which takes two strings&nbsp;<strong>pat, txt,</strong>&nbsp;as input parameters&nbsp;and returns an integer&nbsp;denoting the answer.&nbsp;You don't to print answer or take inputs.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(26) or O(256)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;=&nbsp;|pat| &lt;= |txt|&nbsp;&lt;= 10<sup>5</sup><br>
Both string contains lowercase english letters.</span></p>

<p>&nbsp;</p>
 <p></p>
            </div>
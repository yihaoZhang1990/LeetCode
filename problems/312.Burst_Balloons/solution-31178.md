Python DP N^3 Solutions | LeetCode Discuss
============================
**Author:**  sevensevens
**Reputation:**  27 

<p>Analysis:<br/>
We need to find a way to divide the problems. If we start from the first balloon, we can't determine the left/right for the number in each sub-problem, If we start from the last balloon, we can.<br/>
We can see the transformation equation is very similar to the one for matrix multiplication.</p>
<pre><code>dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) # i &lt; k &lt; j
</code></pre>
<p>This is a typical interval DP problem. Because the order of the number extracted matters, we need to do a O(n^3) DP. If we only need to expand the interval to the left or right, we only need to do a O(n^2) DP.</p>
<p>Top-down:</p>
<pre><code>class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in xrange(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1: # in memory or gap &lt; 2
                return dp[i][j]
            coins = 0
            for k in xrange(i+1, j): # find the last balloon
                coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n-1)
</code></pre>
<p>Bottom-up:</p>
<pre><code> class Solution(object):
        def maxCoins(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            nums = [1] + nums + [1] # build the complete array 
            n = len(nums)
            dp = [[0] * n for _ in xrange(n)]
    
            for gap in xrange(2, n):
                for i in xrange(n-gap):
                    j = i + gap
                    for k in xrange(i+1, j):
                        dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
            return dp[0][n-1]</code></pre> 

Ref: https://discuss.leetcode.com/topic/31178

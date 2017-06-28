# coding=utf-8
# Author: Jianghan LI
# Question: 629.K_Inverse_Pairs_Array
# Date: 2017-06-28
# Complexity: O(NK) O(K)


class Solution(object):

    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        l = n * (n - 1) / 2
        mod = 10**9 + 7
        if n <= 0 or k < 0 or k > l:
            return 0
        k = min(k, l - k)
        if k == 0:
            return 1
        if k == 1:
            return n - 1
        dp = [1]
        for i in range(2, n + 1):
            l = min(i * (i - 1) / 2, k) + 1
            dp2 = [0] * l
            for j in range(l):
                dp2[j] = (dp[j] if j < len(dp) else 0) + (dp2[j - 1] if j else 0) - \
                    (dp[j - i] if -1 < j - i < len(dp) else 0)
                dp2[j] %= mod
            dp = dp2
        return dp[k]

    # shorter
    def kInversePairs(self, n, k, mod=10**9 + 7):
        dp = [1] + [0] * k
        for i in range(2, n + 1):
            dp2 = [0] * (k + 1)
            for j in range(k + 1):
                dp2[j] = (dp[j] + dp2[j - 1] - (dp[j - i] if j - i >= 0 else 0)) % mod
            dp = dp2
        return dp[k]

    # dp, O(NK) O(NK)
    def kInversePairs(self, n, k):
        dp = [[1] + [0] * k for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j] - ((j - i >= 0) and dp[i - 1][j - i]))
        return dp[n][k] % (10**9 + 7)

    # best
    def kInversePairs(self, n, k):
        dp = [1] + [0] * k
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                dp[j] += dp[j - 1]
            for j in range(k, 0, -1):
                dp[j] -= j - i >= 0 and dp[j - i]
        return dp[k] % (10**9 + 7)


############ test case ###########
s = Solution()
# print s.kInversePairs(8, 5)
# print s.kInversePairs(1, 1)
print s.kInversePairs(1000, 1000)

for i in range(10):
    for j in range(i * (i - 1) / 2 + 1):
        print "%3d" % s.kInversePairs(i, j),
    print

############ comments ############
# RuntimeError: maximum recursion depth exceeded

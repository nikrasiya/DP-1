from typing import List
from math import inf


class Solution:
    # Solution works only for canonical coin system
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     coins_set = set(coins)
    #     count = 0
    #     cur_max = -1
    #
    #     if amount == 0:
    #         return 0
    #
    #     while amount > 0 and len(coins_set) > 0:
    #         cur_max = max(coins_set)
    #         if amount - cur_max >= 0:
    #             amount -= cur_max
    #             count += 1
    #         else:
    #             coins_set.remove(cur_max)
    #     if cur_max < 0 or amount != 0:
    #         return -1
    #     return count
    """
        // Time Complexity : O(nk)
                where n is the number of coins and
                      k is the amount range
        // Space Complexity : O(k)
                where k is the amount range
        // Did this code successfully run on Leetcode :
                Yes
        // Any problem you faced while coding this :
                Took time to come up with the Bellman equation
        // Your code here along with comments explaining your approach
                Bellman Equation:
                    OPT[i] = {
                                # if we don't have amount to make change for
                                # we need zero coins, base case
                                0                               i == 0
                                for j in range(len(coins)):
                                        min(1+OPT[i-coin[j]],OPT[i])     if i > coin[j] }
                Sub problems:
                    Each subproblem has the answer to the question- IF I have the iTH amount,
                    the minimum number of coins I will need to make that change.
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf for i in range(0, amount + 1)]
        # base case
        # for an amount of zero, zero coins
        dp[0] = 0
        for coin in coins:
            for j in range(coin, len(dp)):
                dp[j] = min(1 + dp[j - coin], dp[j])
        if dp[-1] == inf:
            return -1
        return dp[-1]

        # OPT = [[None for j in range(0, amount + 1)] for i in range(0, len(coins) + 1)]
        # for k in range(0,len(OPT[0])):
        #     OPT[0][k] = inf
        # for k in range(0, len(OPT)):
        #     OPT[k][0] = 0
        # for i in range(1, len(coins) + 1):
        #     for j in range(1, amount + 1):
        #         if coins[i - 1] > j:
        #             OPT[i][j] = OPT[i - 1][j]
        #         elif coins[i - 1] <= j:
        #             OPT[i][j] = min(OPT[i - 1][j], 1 + OPT[i][j - coins[i - 1]])
        # if OPT[-1][-1] == float('inf'):
        #     return -1
        # return OPT[-1][-1]


if __name__ == '__main__':
    h = Solution()
    print(h.coinChange([2, 7], 10))
    print(h.coinChange([2], 3))
    print(h.coinChange([2147483647], 2))

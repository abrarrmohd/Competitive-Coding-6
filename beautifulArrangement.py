"""
Problem: countArrangement
Approach: recurslive try building all the permutations with the checks for if the conditions of divisibility hold or not
t.c. => n!
s.c. => n
"""
class Solution:
    def countArrangement(self, n: int) -> int:
        used = [False for i in range(n)]

        def helper(l):
            if l == n + 1:
                return 1
            
            ret = 0
            for i in range(1, n + 1):
                if used[i - 1] or ((l%i != 0) and (i%l != 0)):
                    continue

                used[i - 1] = True
                ret += helper(l + 1)
                used[i - 1] = False
            return ret
        return helper(1)
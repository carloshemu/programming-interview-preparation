"""
LeetCode - 1250 - Hard
"""
from typing import List


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        gcd = nums[0]
        for a in nums:
            while a:
              gcd, a = a, gcd % a
        return gcd == 1
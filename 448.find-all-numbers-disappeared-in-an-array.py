#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        print(length)
        comparison_list = list(range(1, length+1))
        print(comparison_list)
        return list(set(comparison_list) - set(nums))

# @lc code=end


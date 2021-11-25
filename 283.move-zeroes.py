#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (59.69%)
# Likes:    7221
# Dislikes: 203
# Total Accepted:    1.4M
# Total Submissions: 2.3M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# Follow up: Could you minimize the total number of operations done?
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def recursiveMover(nums: List[int], index: int, zeroCount: int) -> List[int]:
            if len(nums)-zeroCount == index:
                return 
            elif nums[index] == 0:
                nums.insert(len(nums), nums.pop(index))
                zeroCount+=1
                recursiveMover(nums, index, zeroCount)
            else:
                index+=1
                recursiveMover(nums, index, zeroCount)
        recursiveMover(nums, 0, 0)
            
            
# @lc code=end


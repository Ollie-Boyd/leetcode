#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (48.97%)
# Likes:    16324
# Dislikes: 759
# Total Accepted:    1.9M
# Total Submissions: 3.8M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# A subarray is a contiguous part of an array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: nums = [5,4,-1,7,8]
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
# 
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        record=nums[0]
        if len(nums)==1:
            return nums[0]
        for index, num in enumerate(nums):
            remainingRange=range(index+1, len(nums)+1)
            # print(remainingRange)
            for j in remainingRange:
                # print(nums[index:j])
                total=sum(nums[index:j])
                if total>record:
                    record = total
        return record
# @lc code=end


#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (54.43%)
# Likes:    2014
# Dislikes: 391
# Total Accepted:    549.1K
# Total Submissions: 1M
# Testcase Example:  '[1,1,0,1,1,1]'
#
# Given a binary array nums, return the maximum number of consecutive 1's in
# the array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s. The maximum number of consecutive 1s is 3.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1,0,1]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        record=0
        for b in nums:
            if b==1:
                count+=1
                if count>record:
                    record=count
            else:
                count=0
        return record        
# @lc code=end


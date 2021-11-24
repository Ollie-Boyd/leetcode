#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (60.73%)
# Likes:    4118
# Dislikes: 176
# Total Accepted:    634.7K
# Total Submissions: 1M
# Testcase Example:  '5'
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
# 
# 
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= numRows <= 30
# 
# 
#

# @lc code=start

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        container_array = [[1]]
        while len(container_array) < numRows:
            prev_array = container_array[-1]
            modified_prev_array = list(prev_array)
            modified_prev_array.insert(0,0)
            new_array = [x+y for x,y in zip(prev_array, modified_prev_array)]
            new_array.append(1)
            container_array.append(new_array)
        return container_array
        
# @lc code=end


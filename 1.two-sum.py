#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for (i,num) in enumerate(nums):
            if target-num not in dict:
                dict[num]=i
            else:
                return [dict[target-num],i]
# @lc code=end


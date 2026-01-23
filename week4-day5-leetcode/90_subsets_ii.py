# https://leetcode.com/problems/subsets-ii/

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def helper(index, current):
            result.append(list(current))

            for i in range(index, len(nums)):
                # Skip duplicates
                if i > index and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                helper(i+1, current)
                current.pop()

        helper(0, [])
        return result
    

# Time Complexity O(N * 2^N)
# Space Complexity O(N * 2^N)
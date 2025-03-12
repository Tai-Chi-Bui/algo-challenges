# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.





from typing import List


class Solution:
    # brute force solution
    # O(n²) time, O(1) space
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    
    # hashmap solution  
    # O(n) time, O(n) space
    # def twoSum(self, sums: List[int], target: int) -> List[int]:
    #     hash_sums = {}
    #     for i, num in enumerate(sums):
    #         complement = target - num
    #         if complement in hash_sums:
    #             return [hash_sums[complement], i]
    #         else:
    #             hash_sums[num] = i
    #     return []
    

    # two pointer solution
    # O(n log n) time, O(n) space
    def twoSum(self, sums: List[int], target: int) -> List[int]:
        sorted_sums = [(num, i) for i, num in enumerate(sums)]
        sorted_sums.sort(key=lambda x: x[0])
        left, right = 0, len(sorted_sums) - 1
        while left < right:
            current_sum = sorted_sums[left][0] + sorted_sums[right][0]
            if current_sum == target:
                return [sorted_sums[left][1], sorted_sums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
    

    # conclusion:
    # The hashmap solution is theoretically the most efficient possible solution 
    # because we need to look at each number at least once (O(n)), and we can't do better than that for this problem since we need to consider every element to ensure we don't miss the solution.
            

# test
if __name__ == "__main__": # if the file is run directly, not imported
    solution = Solution()
    nums = [2, 8, 11, 7]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)  # Expected output: [0, 1]



# Given an array of integers nums and an integer target, 
# return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

from typing import List

class Solution:
    def towSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
def main():
    slt = Solution()
    nums = [4,5,6]
    target = 10
    result = slt.towSum(nums, target)
    print(result)

if __name__ == "__main__":
    main()

#comment: cach ng* nhat O(n^2), O(1)
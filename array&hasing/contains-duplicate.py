# Given an integer array nums, 
# return true if any value appears(xuat hien) more than once in the array, 
# otherwise return false.

#example:
# [1,2,3,4] -> True
# [1,2,3,2] -> False
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return False
        return True
    
def main():
    slt = Solution()
    nums = [1,3,2,3,4]
    result = slt.hasDuplicate(nums)
    print(result)

if __name__ == "__main__":
    main()

#comment: voi bai nay co the dung them phuong thuc set() cua python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            first = 0
            second = 0
            while first < len(nums):
                if nums[first] != 0:
                    nums[second] = nums[first]
                    if not first == second:
                        nums[first] = 0
                    second +=1
                first += 1

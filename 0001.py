class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}
        for i in range(len(nums)):
            if nums[i] in dict_num:
                return [dict_num[nums[i]],i]
            dict_num[target - nums[i]] = i

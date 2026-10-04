class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        ans = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i
        #     if target - nums[i] in nums:
        #         ans.append(i)
        # return ans
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #len 1 edge case

        dp =[0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max (nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],nums[i]+ dp[i-2])
        return dp[-1]
        
        # for i  in range(2,len(nums)):
        #     for j in range(i,len(nums),2):
        #         dp[j] = dp[j-1] +dp[j-2]
        #         dp[i] = dp[i-1] + dp[i-2]
        #         if max(dp[i],dp[j]) == dp[i] and j != i: #causes problems cause it leaving last index.
        #         # if max(dp[i],dp[j]) == dp[i] and i+1 < len(nums):
        #             dp[i+1] = dp[j]
        #             # max_sum += dp[j]
        # return max(dp[i],dp[j],max_sum)
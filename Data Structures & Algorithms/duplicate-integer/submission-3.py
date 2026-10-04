class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums =set(nums)
        # if sum(nums) < 0:
        #     nums = nums*-1
        
        # print(set_nums)
        return len(set_nums) != len(nums)
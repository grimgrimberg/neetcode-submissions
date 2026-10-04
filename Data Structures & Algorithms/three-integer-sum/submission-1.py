class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # left, right = 0,len(nums) -1
        # mid = right //2
        # sorted_nums = sorted(nums)
        # set_nums = set(nums)
        # # print(sorted_nums)
        # # print(set_nums)
        # ans = []
        # while left < right:
        #     sum_3 = sorted_nums[left] + sorted_nums[right] + sorted_nums[mid]
        #     if sum_3 >0:
        #         right -=1
        #         mid = (left+right) //2
        #     elif sum_3 == 0:
        #         ans.append([nums[left],nums[mid],nums[right]])
        #     else:
        #         left +=1
        #         ans.append([nums[left],nums[mid],nums[right]])
        # return ans
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return ans

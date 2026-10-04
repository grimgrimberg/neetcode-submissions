class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums) -1
        while high >= low:
            mid = (low + high) //2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]:
                if nums[low]<=target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                                # Is the target within our known sorted right bounds?
                if nums[mid] < target <= nums[high]:
                    low = mid + 1   # Search right
                else:
                    high = mid - 1  # Search left
        return -1
        
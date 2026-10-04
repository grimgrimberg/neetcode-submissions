class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        print(nums_counter)
        ans = []
        for num, freq in nums_counter.most_common(k):
            ans.append(num)

        return ans
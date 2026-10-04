class Solution:

    def backtrack(self,nums, target,seen, sols): 
        if target < 0 :
           return sols
        elif target == 0:
            seen = sorted(seen)
            if seen in sols:
                return sols
            # seen = list(set(seen))
            return sols.append(seen)
        
        for n in nums:

            n2target = self.backtrack(nums,target-n,seen + [n], sols)

        return sols
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sols = []
        sols = self.backtrack(nums,target,[],[])
        return sols



        
    
    
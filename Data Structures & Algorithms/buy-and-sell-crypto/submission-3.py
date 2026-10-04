class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        for right in range(1,len(prices)):
            if prices[left]>prices[right]: #if curr price is lower than buing price, move and buy here
                left =right
            else:
                profit = prices[right]-prices[left]
                if profit> max_profit:
                    max_profit = profit
        return max_profit

        # left, right = 0, len(prices) -1
        # profit,max_profit = 0,0
        # while right > left:
        #     profit = prices[right] - prices[left]
        #     if profit > max_profit:
        #         max_profit = profit
        #         # right -= 1
        #         left+=1
        #     else:
        #         # left+=1
        #         right -= 1

        # return max_profit


        
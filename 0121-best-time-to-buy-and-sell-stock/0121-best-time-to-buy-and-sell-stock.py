class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pro = float('inf')
        max_pro = 0
        
        for i in prices:
            if i < min_pro:
                min_pro = i
            elif (i - min_pro) > max_pro:
                max_pro = i - min_pro
        
        return max_pro

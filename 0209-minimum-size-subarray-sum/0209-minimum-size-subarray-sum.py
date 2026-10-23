class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        low,high,mini,n=0,0,float("inf"),len(nums)
        sum=0
        for high in range(0,n):
            sum+=nums[high]
            while(sum>=target):
                len1=high-low+1
                mini=min(mini,len1)
                sum-=nums[low]
                low+=1
        if mini==float("inf"):
            return 0
        return mini

            





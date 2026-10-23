class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        low,high,n=0,0,len(nums)
        res = float('inf')
        sum=0
        while(high<n):
            sum+=nums[high]
            while(sum>=target):
                len1=(high-low)+1
                res=min(res,len1)
                sum-=nums[low]
                low+=1
            high+=1
        if res==float('inf'):
            return 0

        return res

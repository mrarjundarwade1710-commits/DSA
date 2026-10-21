class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c=0
        co=None
        for i in nums:
            if c==0:
                co=i
            
            c+=(1 if co==i else -1)
        return co

        return candidate
        
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        maxi=nums[0]+nums[1]+nums[2]
        n=len(nums)
        for i in range(n-2):
            left=i+1
            right=n-1
            while(left<right):
                total=nums[i]+nums[left]+nums[right]
                if total == target:
                    return target
                if abs(target-maxi)>abs(target-total):
                    maxi=total
                if (total<target):
                    left+=1
                else:
                    right-=1
                
        return maxi
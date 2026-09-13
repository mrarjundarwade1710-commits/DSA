class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     for j in range(len(nums)-1):
        #         if (nums[j]>nums[j+1]):
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        # O(n^2),No extra space
        low,mid,high=0,0,len(nums)-1
        while(mid<=high):
            if (nums[mid]==0):
                nums[low],nums[mid]=nums[mid],nums[low]
                mid+=1
                low+=1
            elif(nums[mid]==1):
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1

        
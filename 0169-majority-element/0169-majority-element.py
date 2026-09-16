class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # co=0
        # ele=nums[0]
        # for i in nums:
        #     n=nums.count(i)
        #     if co<n:
        #         co=n
        #         ele=i
        # return ele 
        # nums = [2, 2, 1, 1, 1, 2, 2]

        # count = 0         
        # candidate = None        

        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     count += (1 if num == candidate else -1)

        # return candidate
        # nums = [2, 2, 1, 1, 1, 2, 2]
        count=0   
        candi=0   
        for i in range(0,len(nums)):
            if count==0:
                candi=nums[i]
            if  nums[i]==candi:
                count+=1
            else:
                count-=1
        return candi



            # count=count+(1 if i==candi else -1)
            

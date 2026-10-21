class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j,s=0,len(nums)-1,0
        res=sorted(nums)
        val1,val2=0,0
        while(i<j):
            if res[i]+res[j]==target:
                val1,val2=res[i],res[j]
                break
            elif( res[i]+res[j]<target):
                i+=1
            else:
                j-=1
        l=[]
        for k in range(len(nums)):
            if  val1==nums[k] or val2==nums[k]:
                l.append(k)
                if len(l)==2:
                    return l
        return l

                 

                









        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
    #    hash={}
    #    for i,num in enumerate(nums):
    #     con=target-num
    #     if con in hash:
    #         return [hash[con],i]
    #     hash[num]=i


         

                    
        

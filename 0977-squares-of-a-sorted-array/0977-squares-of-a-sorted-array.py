class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # res=[abs(x) for x in nums]
        # res.sort()
        # return [x*x for x in res]
        # return sorted([x*x for x in nums])
        # a=[]
        # b=[]
        # for i in range(len(nums)):
        #     if nums[i]<=0:
        #         a.append(nums[i])
        #     else:
        #         b.append(nums[i])
        # a=[x*x for x in a]
        # a=a[::-1]
        # b=[x*x for x in b]
        # i=len(a)-1
        # j=len(b)-1
        # k=0
        # l=0
        # n=len(nums)
        # res=[0] * n
        # p=0
        # while(k<=i and l<=j):
        #     if a[k]<=b[l]:
        #         res[p]=a[k]
        #         k+=1
        #         p+=1
        #     else:
        #         res[p]=(b[l])
        #         l+=1
        #         p+=1
        # while(k<=i):
        #     res[p]=(a[k])
        #     k+=1
        #     p+=1
        # while(l<=j):
        #     res[p]=(b[l])
        #     l+=1
        #     p+=1
        # return res
        # n=len(nums)
        # l=0
        # r=n-1
        # p=n-1
        # res=[0]* n
        # while(l<=r):
        #     if abs(nums[l]) > abs(nums[r]):
        #         res[p]=nums[l]**2
        #         l+=1
                
        #     else:
        #         res[p]=nums[r]**2
                
        #         r-=1
        #     p-=1
        # return res





        a=[]
        b = []

        for i in range(len(nums)):
            if nums[i] <= 0:
                a.append(nums[i])
            else:
                b.append(nums[i])

        a = [x * x for x in a]
        a = a[::-1]
        b = [x * x for x in b]

        i = len(a) - 1
        j = len(b) - 1
        k = 0
        l = 0

        res = []

        while k <= i and l <= j:
            if a[k] <= b[l]:
                res.append(a[k])
                k += 1
            else:
                res.append(b[l])
                l += 1

        while k <= i:
            res.append(a[k])
            k += 1

        while l <= j:
            res.append(b[l])
            l += 1

        return res

        

        
        
        
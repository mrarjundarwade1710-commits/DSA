class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """ 
        for j in range(n):
            val=nums2[j]
            inserted=False
            for i in range(m):
                if nums1[i]>val:
                    nums1[i+1:m+1]=nums1[i:m]
                    nums1[i]=val
                    m+=1
                    inserted=True
                    break
            if not inserted:
                nums1[m]=val
                m+=1


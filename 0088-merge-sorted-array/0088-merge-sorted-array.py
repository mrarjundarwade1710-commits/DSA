class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c = m   # count of valid elements in nums1

        # loop through nums2 and insert into nums1
        for j in range(n):
            val = nums2[j]
            inserted = False

            # try to insert val into the right place
            for i in range(c):
                if nums1[i] > val:
                    # shift elements to the right
                    nums1[i+1:c+1] = nums1[i:c]
                    nums1[i] = val
                    c += 1
                    inserted = True
                    break

            # if not inserted, append at the end
            if not inserted:
                nums1[c] = val
                c += 1

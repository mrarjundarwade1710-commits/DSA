class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a=[]
        for i in range((numRows)):
            c=[]
            k=0
            for j in range(i+1):
                if (j==i or j==0):
                    c.append(1)
                else:
                    c.append(a[i-1][j-1]+a[i-1][j])
            a.append(c)
        return a

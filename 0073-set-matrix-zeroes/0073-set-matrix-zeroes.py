class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=[]
        c=[]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    r.append(i)
                    c.append(j)
        for i in r:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

    
        for j in c:
            for i in range(len(matrix)):
                matrix[i][j] = 0


                   
        # for i in range(len(a)):
        #     for j in range(len(a[0])):
        #         for p in range(len(matrix)):
        #             for o in range(len(matrix[0])):
        #                     for k in range(len(matrix)):
        #                          matrix[p][k]=0
        #                     for l in range(len(matrix)):
        #                         matrix[l][o]=0
                


                    

        
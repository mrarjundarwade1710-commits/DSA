class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        low,high,n,fr=0,0,len(fruits),{}
        log_sub=float("-inf")
        for high in range(0,n):
            fr[fruits[high]]=fr.get(fruits[high],0)+1
            while( len(fr)>2):
                (fr[fruits[low]])-=1
                if ((fr[fruits[low]])==0):
                    del (fr[fruits[low]])
                low+=1
            if len(fr)<=2:
                log_sub=max(log_sub, high-low+1)
        return log_sub
            

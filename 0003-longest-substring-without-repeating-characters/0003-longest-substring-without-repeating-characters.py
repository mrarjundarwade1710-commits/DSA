class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low,high,n,fr,res=0,0,len(s),{},0
        log_sub=float("-inf")
        if len(s)==0:
            return 0
        for high in range(0,n):
            fr[s[high]]=fr.get(s[high],0)+1
            while(fr[s[high]]>1):
                fr[s[low]]-=1
                if fr[s[low]]==0:
                    del fr[s[low]]
                low+=1
            len1=high-low+1
            log_sub=max(log_sub,len1)
        return log_sub
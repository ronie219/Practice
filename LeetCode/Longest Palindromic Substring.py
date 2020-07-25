class Solution:
    def longestPalindrome(self, s: str) -> str:
        lager=''
        lagerest=''
        
        for i in range(len(s)):
            odd=self.exponcenter(s,i,i)
            evn=self.exponcenter(s,i,i+1)
            larger= odd if len(odd)>len(evn) else evn
            lagerest= lagerest if len(lagerest)>len(larger) else larger
            
        return lagerest
        
        
        
    def exponcenter(self,s,left,right):
        string = ''
        while(left>=0 and right<len(s) and s[left]==s[right]):
            string = s[left:right+1]
            left-=1
            right+=1            
        return string
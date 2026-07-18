class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for i in range(left,right+1):
            temp=list(str(i))
            c,n=0,len(temp)
            if '0' in temp:
                continue
            for j in temp:
                if int(i)%int(j)==0:
                    c+=1
                if c==n:
                    ans.append(i)
        return ans
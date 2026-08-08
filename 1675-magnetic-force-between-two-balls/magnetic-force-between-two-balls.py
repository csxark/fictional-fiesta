class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n,ans=len(position),0
        low,high=1,position[n-1]-position[0]
        while low<=high:
            mid=low+(high-low)//2
            count,pos=1,position[0]
            for i in range(1,n):
                if pos+mid <= position[i]:
                    count+=1
                    pos=position[i]
            if count<m:
                high=mid-1
            else:
                ans=mid
                low=mid+1
        return ans
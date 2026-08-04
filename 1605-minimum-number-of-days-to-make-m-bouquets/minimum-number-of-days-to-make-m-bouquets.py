class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def is_possible(bloom_days,day,m,k):
            count,bouquets=0,0
            for bloom in bloom_days:
                if bloom<=day:
                    count+=1
                    if count==k:
                        bouquets+=1
                        count=0
                else:
                    count=0
            return bouquets>=m

        if m*k>len(bloomDay):
            return -1
        low,high,ans=min(bloomDay),max(bloomDay),-1
        while low<=high:
            mid=low+(high-low)//2
            if is_possible(bloomDay,mid,m,k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
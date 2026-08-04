class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysneeded(weights,capacity):
            days,load=1,0
            for w in weights:
                if load+w>capacity:
                    days+=1
                    load=w
                else:
                    load+=w
            return days
        left,right=max(weights),sum(weights)
        while left<right:
            mid=left+(right-left)//2
            needed=daysneeded(weights,mid)
            if needed<=days:
                right=mid
            else:
                left=mid+1
        return left

            
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sumByD(arr, div):
            return sum(math.ceil(x / div) for x in arr)

        if len(nums) > threshold:
            return -1
        low,high=1,max(nums)
        while low<=high:
            mid=low+(high-low)//2
            if sumByD(nums,mid)<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low
        
        
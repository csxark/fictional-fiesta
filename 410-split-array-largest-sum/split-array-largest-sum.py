class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def count_split(a,max_sum):
            split,subarray_sum=1,0
            for num in a:
                if subarray_sum + num <= max_sum:
                    subarray_sum += num
                else:
                    split += 1
                    subarray_sum = num
            return split

        low,high=max(nums),sum(nums)
        while low<=high:
            mid=(high+low)//2
            splits=count_split(nums,mid)
            if splits>k:
                low=mid+1
            else:
                high=mid-1
        return low

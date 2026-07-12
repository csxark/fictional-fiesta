class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_array(arr,left,right):
            while left<right:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1
        n=len(nums)

        if n==0:
            return 
        k%=n
        if k==0:
            return
        reverse_array(nums,0,n-1)
        reverse_array(nums,0,k-1)
        reverse_array(nums,k,n-1)
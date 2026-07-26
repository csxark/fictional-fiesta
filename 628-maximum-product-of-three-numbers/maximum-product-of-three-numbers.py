class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        m1,m2,m3=nums[-1],nums[-2],nums[-3]
        max_product=m1*m2*m3
        n1,n2,n3=nums[0],nums[1],nums[-1]
        max_product2=n1*n2*n3
        
        return max(max_product,max_product2)

        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter,element,n=0,0,len(nums)
        for i in nums:
            if counter==0:
                counter=1
                element=i
            elif element==i:
                counter+=1
            else:
                counter-=1
        count1=nums.count(element)
        if count1>(n//2):
            return element
        else:
            return -1
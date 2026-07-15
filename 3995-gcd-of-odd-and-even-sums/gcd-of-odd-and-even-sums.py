class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd=(n*n)
        sumEven=(n*(n+1))
        gcd=0
        while sumOdd>0 and sumEven>0:
            if sumOdd>sumEven:
                sumOdd=sumOdd%sumEven
            else:
                sumEven=sumEven%sumOdd
        if (sumOdd==0):
            gcd=sumEven
        else:
            gcd=sumOdd
        return gcd
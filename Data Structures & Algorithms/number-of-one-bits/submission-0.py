class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n:
            if n&1:
                bits+=1
            else:
                bits+=0

            n>>=1

        return bits
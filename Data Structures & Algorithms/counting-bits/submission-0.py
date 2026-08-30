class Solution:
    def countBits(self, n: int) -> List[int]:
       
        result = [0]*(n+1)
        for i in range(1, n+1):
            number = i
            bits = 0
            while number!=0:
                if number&1:
                    bits+=1
                else:
                    bits+=0
                number = number>>1

            result[i] = bits
            
                
        return result
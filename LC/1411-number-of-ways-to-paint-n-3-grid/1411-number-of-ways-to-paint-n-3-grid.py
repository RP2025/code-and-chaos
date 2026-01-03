class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # Either all 3 are different → ABC
        # Only 1st & 3rd match → ABA
        
        # An = 2An-1 + 2Bn-1
        # Bn = 2An-1 + 3Bn-1 
        
        # Base Case -- A,B = 6,6
        
        A = 6
        B = 6
        
        for i in range(2, n + 1):
            newA = (2*A + 2*B) % MOD
            newB = (2*A + 3*B) % MOD
            A, B = newA, newB

        return (A+B)%MOD
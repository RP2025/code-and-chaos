class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #brute approach 
        #check the last digit and increment by one
        #probem will arise when ;ast digit is 9, so there will be a carry that would be forwarded to next digit
        #brute approach would be to take a carry flag, update it whenlast digit is 9 and send it forwaed, however it would be in loop as what is the number is 99999

        #solution 2 that is coming to my mind is do a series of conversion
        #array -> string -> int -> add +1 -> back to string -> array

        # lets make it more optimized,
        # lets do this conversion onmy when needed

        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
            
        return list(map(int, str((int(''.join(map(str, digits))) + 1))))
       
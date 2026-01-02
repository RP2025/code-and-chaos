class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return int((sum(nums)-sum(set(nums)))//((len(nums)/2)-1))
    
    #didn't had time to brainstrom it -- so going brute!
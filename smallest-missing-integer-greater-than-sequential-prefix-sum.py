class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sequence=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                sequence.append(nums[i])         
            else:
                break
        integer=sum(sequence)
        while integer:
            if integer not in nums:
                return integer
            else:
                integer+=1
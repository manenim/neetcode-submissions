class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = j = 0

        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j

        # i, j = 0

        # while i < nums.length:
        #   check if nums[i] != val
        #      nums[i] = nums[j]
        #      j ++
        # i++
        # return j+1
        
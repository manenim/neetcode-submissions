class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, twos = 0, 0, 0

        write_index = 0 

        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            elif num == 2:
                twos += 1
        
        for _ in range(zeros):
            nums[write_index] = 0
            write_index += 1  
        for _ in range(ones):
            nums[write_index] = 1
            write_index += 1
        for _ in range(twos):
            nums[write_index] = 2
            write_index += 1

        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_length = 1
                current_num = num

                while current_num + 1 in num_set:
                    current_length += 1
                    current_num += 1
                
                longest_length = max(current_length, longest_length)
        return longest_length

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(nums):
            comp = target - value 
            print(comp)
            if comp in seen:
                return [seen[comp],  index]
            else:
                seen[value] = index
                
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        final_product = [1] * n
        final_running_prod = 1

        for i in range(1, n):
            fp = nums[i-1] * final_product[i - 1]
            final_product[i] = fp
        for i in range(n-1, -1, -1):
            final_product[i] *= final_running_prod
            final_running_prod *= nums[i]
        return final_product
        
        
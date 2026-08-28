class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        # reverse helper
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1


        # reverse the whole array
        reverse(0, n-1)

        # reverse the first k elements
        reverse(0, k-1)

        # reverse the last k elements
        reverse(k, n-1)


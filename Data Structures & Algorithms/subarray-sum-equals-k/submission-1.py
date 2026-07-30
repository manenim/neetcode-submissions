class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seed = {0: 1}
        notebook = defaultdict(int, seed)
        running_sum = 0
        mark = 0


        for num in nums:
            running_sum += num
            if (running_sum - k) in notebook:
                mark += notebook[(running_sum - k)]
            notebook[running_sum] += 1
        return mark


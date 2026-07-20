class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        seen = defaultdict(int)
        result = 0
        seen[0] = 1

        for num in nums:
            current_sum += num
            target = current_sum - k
            if target in seen:
                result += seen[target]
            seen[current_sum] += 1
        return result


        
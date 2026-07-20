class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_bucket = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)
        result = []
        for item, count in count.items():
            freq_bucket[count].append(item)
        for i in range(len(freq_bucket) -1, 0, -1):
            for num in freq_bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return []
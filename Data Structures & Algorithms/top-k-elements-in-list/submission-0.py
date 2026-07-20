class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = Counter(nums).most_common(k)
        return [item for item, count in nums_dict]
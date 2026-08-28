class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boatCount = 0
        left, right = 0, len(people) - 1
        while left <= right:
            sum_of_weights = people[left] + people[right]
            if sum_of_weights > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            boatCount += 1
        return boatCount
        
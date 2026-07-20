class MyHashSet:

    def __init__(self):
        self.size = 1000

        self.bucket = [[] for _ in range(self.size)]

    def _hash(self, key: int):
        return key % self.size
        

    def add(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.bucket[index]

        if key not in bucket: # must not contain duplicate
            bucket.append(key)

        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.bucket[index]

        if key in bucket:
            bucket.remove(key)
        

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        bucket = self.bucket[index]

        return key in bucket
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
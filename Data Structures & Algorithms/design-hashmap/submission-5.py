class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.bucket = [[] for _ in range(self.size)]
        
    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.bucket[index]

        # the bucket is basically a list of tuples
        for i, (k, v) in enumerate(bucket):
            if key == k:
                bucket[i] = (key, value)
                return 
        bucket.append((key, value))
        

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.bucket[index]

        # the bucket is basically a list of tuples
        for k, v in bucket:
            if key == k:
                return v;
        return -1
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.bucket[index]

        # the bucket is basically a list of tuples
        for i, (k, v) in enumerate(bucket):
            if key == k:
                del bucket[i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
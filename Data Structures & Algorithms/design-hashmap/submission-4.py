class MyHashMap:

    def __init__(self):
        # // define size and empty buckets
        self.size = 1000
        self.bucket = [[] for _ in range(self.size)]

    # define privte hash function
    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.bucket[index]

        for i, (k, v) in enumerate(bucket):

            # if key already exists, update the value otherwise appent key and value tuple to bucket
            if  key == k:
                bucket[i] = (key, value)
                return 
        bucket.append((key, value))
        
        

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.bucket[index]

        for i, (k, v) in enumerate(bucket):

            # if key already exists, update the value otherwise appent key and value tuple to bucket
            if  key == k:
                return v

        return -1 

        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.bucket[index]

        for i, (k, v) in enumerate(bucket):

            # if key already exists, update the value otherwise appent key and value tuple to bucket
            if  key == k:
                del bucket[i]
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
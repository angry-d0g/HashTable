
class Hash_Table:
    def __init__(self, size):
        self.size = size
        self.create()

    def create(self):
        self.table = [[], ] * self.size

    def hashFunction(self, key):
        # capacity = self.getPrime(self.size)
        # return key % capacity
        number = 0
        for i in range(len(key)-1):
            number += ord(key[i])
        return number % self.size

    def set(self, key, data):
        index = self.hashFunction(key)
        for i in range(self.size - 1):
            k = index + i
            if k >= self.size:
                k = k - self.size - 1

            if self.table[k] == [] or self.table[k][0] == key:
                self.table[k] = [key, data]
                break
            elif self.table[k] == [key, data]:
                break

    def delete(self, key):
        index = self.hashFunction(key)
        for i in range(self.size - 1):

            k = index + i
            if k >= self.size:
                k = k - self.size - 1

            if self.table[k][0] == key:
                self.table[k] = [0, 0]
                break

    def get(self, key):
        index = self.hashFunction(key[0])
        for i in range(self.size - 1):

            k = index + i
            if k >= self.size:
                k = k - self.size - 1

            if self.table[k] == []:
                return None

            if self.table[k][0] == key:
                return self.table[k][1]


db = Hash_Table(10)
db.set("apple", 123)
db.set("ananas", 123)
db.set("aaaa", 123)
db.set("aaaa", 123)
db.delete("apple")
db.set("aaa", 123)

print(db.table)
print(db.get("ananas"))


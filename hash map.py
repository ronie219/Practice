<<<<<<< HEAD
class HashTable:

    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, keys):
        hash = 0
        for key in keys:
            hash += ord(key)
        return hash % self.MAX

    def __getitem__(self, key):
        idx = self.get_hash(key)
        for i in self.arr[idx]:
            if i[0] == key:
                return i[1]
        raise KeyError

    def __setitem__(self, key, value):
        idx = self.get_hash(key)
        found = False
        """
        Implementation of liner chaining for the data collision  
        """
        for indx, element in enumerate(self.arr[idx]):
            if element[0] == key:
                found = True
                self.arr[idx][indx] = (key, value)
                break
        if not found:
            self.arr[idx].append((key, value))


t = HashTable()
t['march 11'] = "Abhishek"
t['march 10'] = "Atul"
t['march 17'] = "Biswas"
t['march 6'] = "overrite"
t['march 6'] = "overrite 2"

print(t['march 11'])
print(t['march 10'])
print(t['march 17'])
print(t['march 6'])
print(t['march 18'])

print(t.arr)

=======
class HashTable:

    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, keys):
        hash = 0
        for key in keys:
            hash += ord(key)
        return hash % self.MAX

    def __getitem__(self, key):
        idx = self.get_hash(key)
        for i in self.arr[idx]:
            if i[0] == key:
                return i[1]
        raise KeyError

    def __setitem__(self, key, value):
        idx = self.get_hash(key)
        found = False
        """
        Implementation of liner chaining for the data collision  
        """
        for indx, element in enumerate(self.arr[idx]):
            if element[0] == key:
                found = True
                self.arr[idx][indx] = (key, value)
                break
        if not found:
            self.arr[idx].append((key, value))


t = HashTable()
t['march 11'] = "Abhishek"
t['march 10'] = "Atul"
t['march 17'] = "Biswas"
t['march 6'] = "overrite"
t['march 6'] = "overrite 2"

print(t['march 11'])
print(t['march 10'])
print(t['march 17'])
print(t['march 6'])
print(t['march 18'])

print(t.arr)

>>>>>>> 7f688d62f8ef42d5982882d6981075fb426ea81a

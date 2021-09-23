"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, value, key):
        """Input a string that's stored in
        the table."""
        hash = self.calculate_hash_value(key)
        if not self.table[hash]:
            self.table[hash] = [(key, value)]
            return
        return self.table[hash].append((key,value))

    def lookup(self, key):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash = self.calculate_hash_value(key)
        bag = self.table[hash]
        found = [] if not bag else [i for i in bag if i[0] == key]
        if len(found) > 0:
            return found[0][1]
        raise ValueError(f"key: {key} does not exist")

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return (ord(string[:1])*100) + ord(string[1:2])

# Setup
hash_table = HashTable()

# Store something
hash_table.store(key="UDA", value=123)
hash_table.store(key="UDAC", value=1234)

print(
    hash_table.lookup("UDA"),
    hash_table.lookup("UDAC"),
    hash_table.lookup("UDACI"),
)

class RandomizedSet:

    def __init__(self):
        self.st = set()

    def insert(self, val: int) -> bool:
        if val in self.st: return False
        self.st.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.st:
            self.st.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        # We are only accessing the element, no modifying it.
        # So, we can use both list and tuple to achieve this.
        # But, "tuple" is faster than "list" because of its static nature.
        # That's why I used tuple here!
        return random.choice(tuple(self.st))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
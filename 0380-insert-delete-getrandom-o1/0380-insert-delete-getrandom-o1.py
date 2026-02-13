class RandomizedSet:

    def __init__(self):
        self._set=[]
        self._map={}
    
    def insert(self, val: int) -> bool:
        if val in self._map:
            return False
        self._map[val]=len(self._set)
        self._set.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self._map:
            idx=self._map[val]
            last_elt=self._set[-1]

            self._set[idx] = last_elt
            self._map[last_elt] = idx
            
            self._set.pop()
            del self._map[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self._set)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
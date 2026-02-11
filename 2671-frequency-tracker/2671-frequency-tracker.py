class FrequencyTracker:

    def __init__(self):
        self.counts = {}
        self.freq_map = {}

    def add(self, number: int) -> None:
        old_freq = self.counts.get(number, 0)
        new_freq = old_freq + 1
        
        self.counts[number] = new_freq
        
        
        if old_freq in self.freq_map:
            self.freq_map[old_freq] -= 1
        
        
        self.freq_map[new_freq] = self.freq_map.get(new_freq, 0) + 1

    def deleteOne(self, number: int) -> None:
        if number in self.counts and self.counts[number] > 0:
            old_freq = self.counts[number]
            new_freq = old_freq - 1
            self.counts[number] = new_freq
           
            self.freq_map[old_freq] -= 1
            self.freq_map[new_freq] = self.freq_map.get(new_freq, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
      
        return self.freq_map.get(frequency, 0) > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
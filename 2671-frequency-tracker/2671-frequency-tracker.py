class FrequencyTracker:

    def __init__(self):
        self.count={}
        self.freq={}

    def add(self, number: int) -> None:
        old_freq=self.count.get(number,0)
        new_freq=old_freq+1
        self.count[number]=new_freq
        if old_freq in self.freq:
            self.freq[old_freq]-=1
        self.freq[new_freq]=self.freq.get(new_freq,0)+1

        

    def deleteOne(self, number: int) -> None:
        if number in self.count and self.count[number]>0:
            old_freq=self.count.get(number,0)
            new_freq=old_freq-1
            self.count[number]=new_freq
            if old_freq in self.freq:
                 self.freq[old_freq]-=1
            self.freq[new_freq]=self.freq.get(new_freq,0)+1

        

    def hasFrequency(self, frequency: int) -> bool:
        if self.freq.get(frequency,0)>0:
            return True
        return False       


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
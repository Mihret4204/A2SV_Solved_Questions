class RecentCounter:

    def __init__(self):
        self.start=0
        self.que=[]

    def ping(self, t: int) -> int:
        self.que.append(t)
        while t-self.que[self.start]>3000:
            self.start+=1
        return len(self.que)-self.start

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
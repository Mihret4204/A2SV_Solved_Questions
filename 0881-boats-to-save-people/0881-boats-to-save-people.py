class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i=0
        j =len(people)-1
        n=0
        while i<=j:
            if people[i]+people[j]<=limit:
                j-=1
            n+=1
            i+=1
        return n
            
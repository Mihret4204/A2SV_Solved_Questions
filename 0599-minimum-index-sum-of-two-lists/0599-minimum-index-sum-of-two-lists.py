class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        n=float(inf)
        name=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                min=i+j
                if list1[i]==list2[j] and min<n:
                    name=[list1[i]]
                    n=min
                elif list1[i]==list2[j] and min==n:
                    name.append(list1[i])
                    
        return name
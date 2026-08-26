class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        st = min(start,destination)
        end = max(start,destination)
        s = sum(distance)
        x = sum(distance[st:end])
        
        return min(x, s-x)
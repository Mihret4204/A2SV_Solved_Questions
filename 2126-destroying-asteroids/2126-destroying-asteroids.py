class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        pow = mass
        asteroids.sort()
        for a in asteroids:
            if pow < a:
                return False
            if pow >= 10**5:
                return True
            pow+=a
        return True
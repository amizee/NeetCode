class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            cars.append((p, s))
        cars.sort(key=lambda car: car[0], reverse=True)

        stack = []
        for c in cars:
            position, speed = c[0], c[1]
            time = (target - position) / speed
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)

# Intuition: sort cars by closest to the target since they will finish first. The top of the stack maintains the current time required to reach the target. Any car that can reach the target <= this time
# will catch up to this car, forming a car fleet. Otherwise, it forms its own car fleet and this time is pushed onto the top of the stack to find other cars that may join this fleet.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_pairs = [[pos, sp] for pos, sp in zip(position, speed)]
        car_fleets = []

        for pos, sp in sorted(car_pairs, reverse=True):
            car_fleets.append((target - pos) / sp)

            if len(car_fleets) >= 2 and car_fleets[-1] <= car_fleets[-2]:
                car_fleets.pop()

        return len(car_fleets)
class Solution:

    def carFleet(
        self, target: int, position: List[int], speed: List[int]
    ) -> int:
        # 1. Pair up each car's position with its speed
        # Example: position [10, 8], speed [2, 4] -> [(10, 2), (8, 4)]
        cars = list(zip(position, speed))

        # 2. Sort cars by their starting position in REVERSE order (closest to finish line first)
        # We start from the front because the lead cars dictate the traffic speed.
        cars.sort(reverse=True)

        fleets = []

        for pos, spd in cars:
            # 3. Calculate how long it takes this car to finish if alone
            time_to_finish = (target - pos) / spd

            # 4. Check if this car bumps into the fleet ahead of it
            # If 'fleets' is empty, this is the lead car. It forms the first fleet.
            if not fleets:
                fleets.append(time_to_finish)
            else:
                # If this car's alone-time is LESS than or EQUAL to the fleet ahead of it...
                # it means this car is faster/catches up, so it joins that fleet.
                # We don't add its time to the list because it is trapped behind the slower leader.
                if time_to_finish > fleets[-1]:
                    # It takes longer than the car ahead, so it can NEVER catch up.
                    # It starts its own brand-new fleet.
                    fleets.append(time_to_finish)

        # 5. The number of remaining finish times is our total number of fleets
        return len(fleets)
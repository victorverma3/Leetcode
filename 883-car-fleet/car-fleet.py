class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if len(position) == 1:
            return 1

        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = sorted(cars, key=lambda car: car[0], reverse=True)

        hours = [(target - car[0]) / float(car[1]) for car in cars]
        curr_hour = hours[0]
        fleets = 1
        for i in range(1, len(hours)):
            if hours[i] <= curr_hour:
                continue
            else:
                fleets += 1
                curr_hour = hours[i]
        
        return fleets
        
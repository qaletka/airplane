import random
from plane import Plane


class Airline:
    def __init__(self, list_of_planes: list[Plane]):
        self.planes = list_of_planes

    def get_available_seats_of_all_planes(self):
        output = 0
        for plane in self.planes:
            output += plane.get_available_seats()
        return output


if __name__ == '__main__':
    planes = []
    for i in range(10):
        plane = Plane(f"plane_{i}", random.randint(100, 200))
        planes.append(plane)
    airline = Airline(planes)
    print(airline.get_available_seats_of_all_planes())
  

class Plane:
  
    def __init__(self, name, number_of_seats):
        self.name = name
        self.number_of_seats = number_of_seats
        self.total_flew_distance = 0
        self.number_of_occupied_seats = 0

    def fly(self, distance):
        self.total_flew_distance += distance

    def is_service_required(self):
        return self.total_flew_distance > 10000

    def board_passengers(self, number_of_passengers):
        if number_of_passengers + self.number_of_occupied_seats <= self.number_of_seats:
            self.number_of_occupied_seats = number_of_passengers + self.number_of_occupied_seats
        else:
            self.number_of_occupied_seats = self.number_of_seats

    def get_available_seats(self):
        return self.number_of_seats - self.number_of_occupied_seats


if __name__ == '__main__':
  

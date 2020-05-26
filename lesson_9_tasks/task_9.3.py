class Car:

    def __init__(self, model, engine_type, max_speed, count_of_passengers, color):
        self.model = model
        self.engine_type = engine_type
        self.max_speed = max_speed
        self.count_of_passengers = count_of_passengers
        self.color = color
    
    def move(self):
        print(f'The {self.color} {self.model} is moving')
    
    def stop_engine(self):
        print(f'The {self.model} has been stopped')
    
    def get_max_speed(self):
        print(f'Max speed is {self.max_speed}')
    
    def get_count_of_passengers(self):
        print(f'The car {self.model} can accommodate {self.count_of_passengers} passengers')

class Truck(Car):

    def move(self):
        print('Truck is moving')

    def offload(self):
        print('The items are being offloaded')

    def increment_speed(self, value):
        self.max_speed += value
    
    def load(self):
        print('The truck was loaded')

class Passenger_car(Car):

    def move(self):
        print(f'Passenger {self.color} {self.model} is moving')
    
    def parking(self):
        print(f'Passenger {self.color} {self.model} was parked')

    def refuele_the_car(self):
        print(f'Passenger {self.color} {self.model} was refueled')
    
    def increment_passengers(self, count):
        self.count_of_passengers += count
    

car = Passenger_car('mersedes', 'dQ-1', 240, 4, 'black')

car.move()
car.stop_engine()
car.parking()
car.increment_passengers(2)
car.get_count_of_passengers()
car.refuele_the_car()
    

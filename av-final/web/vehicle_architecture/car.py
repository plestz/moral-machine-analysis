from enum import Enum
from "../web/person_architecture" import Passenger

class VehicleCondition(Enum):
    BROKEN = 0
    VERY_DAMAGED = 1
    DAMAGED = 2
    DENTED = 3
    OK = 4
    GOOD = 5
    GREAT = 6
    FANTASTIC = 7
    NEW = 8

class Car:
    def __init__(self, make: str, model: str, nickname: str, color: str, price: float, year_made: int, year_sold: int, condition: VehicleCondition, distance_traveled: float, num_passengers: int, passengers: "list[Passenger]", curr_speed: float):
        self.make = make
        self.model = model
        self.nickname = "Unknown"
        self.color = color
        self.price = price
        self.year_made = year_made
        self.year_sold = year_sold
        self.condition = condition
        self.distance_traveled = distance_traveled # MPH
        self.num_passengers = num_passengers
        self.passengers = passengers
        self.curr_speed = curr_speed # MPH
        self.engine_running = False

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            print("Engine started.")
        else:
            print("Engine already running.")

    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            print("Engine stopped.")
        else:
            print("Engine already stopped.")

    def accelerate(self, speed_increase: float):
        if self.engine_running:
            self.curr_speed += speed_increase
            print(f"Accelerated to {self.curr_speed} MPH.")
        else:
            print("Engine not running. Start the engine first.")

    def decelerate(self, speed_decrease: float):
        if self.engine_running:
            self.curr_speed -= speed_decrease
            print(f"Decelerated to {self.curr_speed} MPH.")
        else:
            print("Engine not running. Start the engine first.")

    def add_passenger(self, passenger: Passenger):
        self.passengers.append(passenger)
        self.num_passengers += 1
        print(f"{passenger.name} has entered the car. There are now {self.num_passengers} passengers in the car.")

    def remove_passenger(self, passenger: Passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            self.num_passengers -= 1
            print(f"{passenger.name} has exited the car. There are now {self.num_passengers} passengers in the car.")
        else:
            print(f"{passenger.name} is not in the car.")


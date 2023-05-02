from enum import Enum

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

class Vehicle:
    def __init__(self, make: str, model: str, nickname: str, color: str, price: float, year_made: int, year_sold: int, condition: VehicleCondition, distance_traveled: float):
        self.make = make
        self.model = model
        self.nickname = "Unknown"
        self.color = color
        self.price = price
        self.year_made = year_made
        self.year_sold = year_sold
        self.condition = condition
        self.distance_traveled = distance_traveled

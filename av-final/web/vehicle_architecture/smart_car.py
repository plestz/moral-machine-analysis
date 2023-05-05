import random
from enum import Enum
from car import Car
from person import Person
from passenger import Passenger
from pedestrian import Pedestrian
from person import Class
from car import VehicleCondition

class Region(Enum):
    WESTERN = 0
    EASTERN = 1
    SOUTHERN = 2

class Decision(Enum):
    PROTECT_PASSENGERS = 0
    PROTECT_PEDESTRIANS = 1

class SmartCar(Car):
    def __init__(self, make: str, model: str, nickname: str, color: str, price: float, year_made: int, year_sold: int, condition: VehicleCondition, distance_traveled: float, num_passengers: int, passengers: "list[Passenger]", curr_speed: float, region: Region):
        super().__init__(make, model, nickname, color, price, year_made, year_sold, condition, distance_traveled, num_passengers, passengers, curr_speed)
        self.activate_engine()
        self.vehicle_on = True
        self.activate_computer()
        self.region = region


    def activate_computer(self):
        pass # Must not be infinite loop for testing purposes
        # while(self.vehicle_on):
        #     self.run()

    def make_decision(self, pedestrians: "list[Pedestrians]" = None) -> Decision:
        passengers, _ = self.collect_decision_data(pedestrians)
        pedestrians = pedestrians if pedestrians else self.collect_decision_data()
        return self.calculate_mean_decision(passengers, pedestrians)

    def collect_decision_data(self, pedestrians: "list[Pedestrian]" = None):
        v_passengers: "list[Passenger]" = passengers if passengers else self.passengers
        v_pedestrians: "list[Pedestrian]" = pedestrians if pedestrians else self.survey_environment()

        return (v_passengers, v_pedestrians)

    def calculate_mean_decision(self, passengers: "list[Passenger]", pedestrians: "list[Pedestrian]"):
        tot_passenger_value = sum([self.calculate_human_value(passenger) for passenger in passengers])
        avg_passenger_value = tot_passenger_value / len(passengers)

        print("tot_passenger_value", tot_passenger_value)
        print("avg_passenger_value", avg_passenger_value)

        tot_pedestrian_value = sum([self.calculate_human_value(pedestrian) for pedestrian in pedestrians])
        avg_pedestrian_value = tot_pedestrian_value / len(pedestrians)

        print("tot_pedestrian_value", tot_pedestrian_value)
        print("avg_pedestrian_value", avg_pedestrian_value)

        # return Decision.PROTECT_PASSENGERS if (avg_passenger >= avg_pedestrian_value) else Decision.PROTECT_PEDESTRIANS
        return Decision.PROTECT_PASSENGERS if ((300 * len(passengers) + avg_passenger_value) >= (300 * len(pedestrians) + avg_pedestrian_value)) else Decision.PROTECT_PEDESTRIANS
        # return Decision.PROTECT_PASSENGERS if ((400 * len(passengers) + avg_passenger_value) >= (400 * len(pedestrians) + avg_pedestrian_value)) else Decision.PROTECT_PEDESTRIANS

    def calculate_human_value(self, person: Person) -> int:
        age_bias, weight_bias, class_bias, law_bias = self.get_regional_bias(person)
        return (((100 - person.age) if person.age >= 30 else (person.age + 20)) + age_bias) \
                + (((300 - int(person.weight)) if person.age >= 18 else 100) + weight_bias) \
                + (150 + person.education_level * 10) \
                + (400 if person.is_doctor else 0) \
                + (300 if person.employed else 0) \
                + (200 if person.married else 0) \
                + (150 * person.num_children) \
                + (20 * person.num_living_relatives) \
                + ((-300 if person.actively_breaking_law else 0) + law_bias) \
                + class_bias

    def get_regional_bias(self, person: Person):
        regional_age_bias = None
        regional_weight_bias = None
        regional_class_bias = None
        regional_law_bias = None

        match self.region:
            case Region.WESTERN:
                regional_age_bias = 180
                regional_weight_bias = 180
                regional_class_bias = person.wealth_class.value * 40
                regional_law_bias = 40
            case Region.EASTERN:
                regional_age_bias = -200
                regional_weight_bias = -200
                regional_class_bias = 0
                regional_law_bias = 300
            case Region.SOUTHERN:
                regional_age_bias = 300
                regional_weight_bias = 180
                regional_class_bias = person.wealth_class.value * 120
                regional_law_bias = 40

        return (regional_age_bias, regional_weight_bias, regional_class_bias, regional_law_bias)



    def activate_engine(self): # Implementation irrelevant to project
        pass

    def survey_environment(self): # Implementation irrelevant to project
        pass

    def run(self): # Implementation irrelevant to project
        pass


        
if __name__ == '__main__':
    people: "list[People]" = Person.get_people(100)
    num_passengers = random.randint(1, 5)
    num_pedestrians = random.randint(1, 5)
    passengers: "list[Passenger]" = random.sample(people, num_passengers)
    pedestrians: "list[Pedestrian]" = random.sample(people, num_pedestrians)

    # self, make: str, model: str, nickname: str, color: str, price: float, year_made: int, year_sold: int, condition: VehicleCondition, distance_traveled: float, num_passengers: int, passengers: "list[Passenger]", curr_speed: float, region: Region
    western_car = SmartCar("Honda", "Civic", "The Red Racer", "Red", 20000, 2022, 2023, VehicleCondition.NEW, 0, num_passengers, passengers, 50, Region.WESTERN)
    eastern_car = SmartCar("Toyota", "Corolla", "Green Machine", "Green", 18000, 2021, 2022, VehicleCondition.GREAT, 10000, num_passengers, passengers, 50, Region.EASTERN)
    southern_car = SmartCar("Ford", "Focus", "Blue Lightning", "Blue", 25000, 2020, 2023, VehicleCondition.GOOD, 30000, num_passengers, passengers, 50, Region.SOUTHERN)

    print("passengers")
    print()
    for passenger in passengers:
        print(passenger)
        print('---------------------------------------')
    print("pedestrians")
    print()
    for pedestrian in pedestrians:
        print(pedestrian)
        print('---------------------------------------')

    western_decision = western_car.make_decision(pedestrians)
    eastern_decision = eastern_car.make_decision(pedestrians)
    southern_decision = southern_car.make_decision(pedestrians)
    print("num_passengers: ", num_passengers)
    print("num_pedestrians: ", num_pedestrians)

    print("Western Decision: ", western_decision)
    print("Eastern Decision: ", eastern_decision)
    print("Southern Decision: ", southern_decision)
from enum import Enum
from "av-final/web/person_architecture" import Passenger, Pedestrian, Person

class Region(Enum):
    WESTERN = 0
    EASTERN = 1
    SOUTHERN = 2

class Decision(Enum):
    PROTECT_PASSENGERS = 0
    PROTECT_PEDESTRIANS = 1

class SmartCar(Car):
    def __init__(self, region: Region):
        super().__init__()
        self.activate_engine()
        self.activate_computer()
        self.region = region
        self.vehicle_on = True

    def activate_computer(self):
        while(self.vehicle_on):
            self.run()

    def make_decision(self) -> Decision:
        passengers, pedestrians = self.collect_decision_data()
        return self.calculate_mean_decision(passengers, pedestrians)

    def calculate_mean_decision(self, passengers: "list[Passenger]", pedestrians: "list[Pedestrian]"):
        tot_passenger_value = sum([self.calculate_value(passenger) for passenger in passengers])
        avg_passenger_value = tot_passenger_value / len(passengers)

        tot_pedestrian_value = sum([self.calculate_value(pedestrian) for pedestrian in pedestrian])
        avg_pedestrian_value = tot_pedestrian_value / len(pedestrian)

        return PROTECT_PASSENGERS 
               if avg_pedestrian_value >= avg_pedestrian_value 
               else PROTECT_PEDESTRIANS


    def collect_decision_data(self, passengers: "list[Passenger]" = None, pedestrians: "list[Pedestrian]" = None):
        v_passengers: "list[Passenger]" = passengers if passengers else self.passengers
        v_pedestrians: "list[Pedestrian]" = pedestrians if pedestrians else self.survey_environment()

        return v_passengers, v_pedestrians

    def calculate_value(self, person: Person) -> int:
        return ((100 - self.age) if self.age >= 30 else (self.age + 20)) \
                + (300 - int(self.weight))
                + (200 + self.education_level * 10)
                + (400 if self.is_doctor else 0)
                + (300 if self.employed else 0)
                + (200 if self.married else 0)
                + (100 * self.num_children)
                + (20 * self.num_living_relatives)
                + (-400 if actively_breaking_law else 0)

    def get_regional_bias(self):
        regional_age_bias = None
        regional_weight_bias = None
        regional_weight_bias = None

        match self.region:
            case Region.WESTERN:

            case Region.EASTERN:
            case Region.SOUTHERN:




    def activate_engine(self): # Implementation irrelevant to project
        pass

    def survey_environment(self): # Implementation irrelevant to project
        pass

    def run(self): # Implementation irrelevant to project
        pass

        
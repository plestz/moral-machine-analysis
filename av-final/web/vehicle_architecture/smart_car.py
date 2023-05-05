from enum import Enum
from "av-final/web/person_architecture" import Passenger, Person

class Decision(Enum):
    PROTECT_PASSENGERS = 0
    PROTECT_PEDESTRIANS = 1

class SmartCar(Car):
    def __init__(self):
        super().__init__()
        self.activate_engine()
        self.activate_computer()
        self.vehicle_on = True

    def activate_computer(self):
        while(self.vehicle_on):
            self.run()

    def make_decision(self) -> Decision:
        passengers, pedestrians = self.collect_decision_data()
        return self.calculate_mean_decision(passengers, pedestrians)

    def calculate_mean_decision(self, passengers: "list[Passenger]", pedestrians: "list[Pedestrian]"):
        pass

    def collect_decision_data(self):
        passengers: "list[Passenger]" = self.passengers
        pedestrians: "list[Pedestrian]" = self.survey_environment()

        return passengers, pedestrians


    def activate_engine(self): # Implementation irrelevant to project
        pass

    def run(self):
        pass

        
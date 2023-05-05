from enum import Enum
from "av-final/web/person_architecture" import Passenger, Pedestrian, Person

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
        tot_passenger_value = sum([calculate_value(passenger) for passenger in passengers])
        avg_passenger_value = tot_passenger_value / len(passengers)

        tot_pedestrian_value = sum([calculate_value(pedestrian) for pedestrian in pedestrian])
        avg_pedestrian_value = tot_pedestrian_value / len(pedestrian)

        return PROTECT_PASSENGERS 
               if avg_pedestrian_value >= avg_pedestrian_value 
               else PROTECT_PEDESTRIANS


    def collect_decision_data(self, passengers: "list[Passenger]" = None, pedestrians: "list[Pedestrian]" = None):
        v_passengers: "list[Passenger]" = passengers if passengers else self.passengers
        v_pedestrians: "list[Pedestrian]" = pedestrians if pedestrians else self.survey_environment()

        return v_passengers, v_pedestrians


    def activate_engine(self): # Implementation irrelevant to project
        pass

    def survey_environment(self): # Implementation irrelevant to project
        pass

    def run(self): # Implementation irrelevant to project
        pass

        
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

    def collect_decision_data(self, passengers: "list[Passenger]" = None, pedestrians: "list[Pedestrian]" = None):
        v_passengers: "list[Passenger]" = passengers if passengers else self.passengers
        v_pedestrians: "list[Pedestrian]" = pedestrians if pedestrians else self.survey_environment()

        return (v_passengers, v_pedestrians)

    def calculate_mean_decision(self, passengers: "list[Passenger]", pedestrians: "list[Pedestrian]"):
        tot_passenger_value = sum([self.calculate_human_value(passenger) for passenger in passengers])
        avg_passenger_value = tot_passenger_value / len(passengers)

        tot_pedestrian_value = sum([self.calculate_human_value(pedestrian) for pedestrian in pedestrian])
        avg_pedestrian_value = tot_pedestrian_value / len(pedestrian)

        return PROTECT_PASSENGERS 
               if (400 * len(passengers) + avg_pedestrian_value) 
               >= (400 * len(pedestrians) + avg_pedestrian_value) 
               else PROTECT_PEDESTRIANS

    def calculate_human_value(self, person: Person) -> int:
        age_bias, weight_bias, class_bias, law_bias = self.get_regional_bias(person)
        return (((100 - person.age) if person.age >= 30 else (person.age + 20)) + age_bias) \
                + (((300 - int(person.weight)) if self.age >= 18 else 100) + weight_bias)
                + (150 + person.education_level * 10)
                + (400 if person.is_doctor else 0)
                + (300 if person.employed else 0)
                + (200 if person.married else 0)
                + (100 * person.num_children)
                + (20 * person.num_living_relatives)
                + ((-300 if person.actively_breaking_law else 0) + law_bias)
                + class_bias

    def get_regional_bias(self, person: Person):
        regional_age_bias = None
        regional_weight_bias = None
        regional_class_bias = None
        regional_law_bias = None

        match self.region:
            case Region.WESTERN:
                regional_age_bias = 90
                regional_weight_bias = 90
                regional_class_bias = person.wealth_class.value * 20
                regional_law_bias = 20
            case Region.EASTERN:
                regional_age_bias = -100
                regional_weight_bias = -100
                regional_class_bias = 0
                regional_law_bias = 150
            case Region.SOUTHERN:
                regional_age_bias = 150
                regional_weight_bias = 90
                regional_class_bias = person.wealth_class.value * 60
                regional_law_bias = 20

        return (regional_age_bias, regional_weight_bias, regional_class_bias, regional_law_bias)



    def activate_engine(self): # Implementation irrelevant to project
        pass

    def survey_environment(self): # Implementation irrelevant to project
        pass

    def run(self): # Implementation irrelevant to project
        pass


        
if __name__ == '__main__':
    people: "list[People]" = Person.get_people(100)
    passengers: "list[Passenger]" = random.sample(people, num_passengers)
    pedestrians: "list[Pedestrian]" = random.sample(people, num_pedestrians)
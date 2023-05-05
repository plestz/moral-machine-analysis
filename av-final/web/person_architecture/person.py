from enum import Enum

class Class(Enum):
    IMPOVERISHED = 0
    LOWER = 1
    LOWER_MIDDLE = 2
    MIDDLE = 3
    UPPER_MIDDLE = 4
    UPPER = 5
    ELITE = 6

class Person:
    def __init__(self, name: str, age: int, gender: str, weight: float, education_level: int, occupation: str, is_doctor: bool, employed: bool, wealth_class: Class, married: bool, num_children: int, num_living_relatives: int, actively_breaking_law: bool):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.education_level = education_level
        self.occupation = occupation
        self.is_doctor = is_doctor
        self.employed = employed
        self.wealth_class = wealth_class # CONTROVERSIAL
        # self.net_worth = net_worth
        # self.societal_impact = societal_impact
        # self.nationality = nationality
        # self.ethnicity = ethnicity
        self.married = married
        self.num_children = num_children
        self.num_living_relatives = num_living_relatives
        self.actively_breaking_law = actively_breaking_law

    
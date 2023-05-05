class Person:
    def __init__(self, name: str, age: int, gender: str, weight: float, education_level: int, occupation: str, is_doctor: bool, married: bool, num_children: int, num_living_relatives: int, actively_breaking_law: bool):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.education_level = education_level
        self.occupation = occupation
        self.is_doctor = is_doctor
        self.employed = employed
        # self.net_worth = net_worth
        # self.societal_impact = societal_impact
        # self.nationality = nationality
        # self.ethnicity = ethnicity
        self.married = married
        self.num_children = num_children
        self.num_living_relatives = num_living_relatives
        self.actively_breaking_law = actively_breaking_law

    def calculate_value(self) -> int:
        return (100 - self.age) \
                + (300 - int(self.weight))
                + (200 + self.education_level * 10)
                + (400 if self.is_doctor else 0)
                + (300 if self.employed else 0)
                + (200 if self.married else 0)
                + (100 * self.num_children)
                + (20 * self.num_living_relatives)
                + (-400 if actively_breaking_law else 0)


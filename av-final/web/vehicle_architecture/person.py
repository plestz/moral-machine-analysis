import random
import numpy as np
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

    @staticmethod
    def get_people(num_people: int) -> "list[Person]":
        people = []
        occupations = ['Engineer', 'Doctor', 'Teacher', 'Cashier', 'Police Officer', 'Unemployed', 'Chef', 'Artist', 'Salesperson', 'Journalist', 'Manager', 'Scientist', 'Programmer']

        for _ in range(num_people):
            first_name = random.choice(['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Harper', 'Evelyn', 'Liam', 'Noah', 'William', 'James', 'Oliver', 'Benjamin', 'Elijah', 'Lucas', 'Mason', 'Logan'])
            last_name = random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin'])
            name = first_name + " " + last_name
            age = random.randint(0, 100)
            gender = random.choice(['M', 'F', 'Non-binary'])
            
            if age < 2:
                weight = round(random.uniform(7, 20), 1)
            elif age < 10:
                weight = round(random.uniform(20, 80), 1)
            elif age < 20:
                weight = round(random.uniform(70, 200), 1)
            else:
                weight = round(random.uniform(100, 230), 1)

            education_level = random.randint(0, 20)
            occupation = 'Student' if age <= 18 else random.choice(occupations)
            is_doctor = occupation == 'Doctor'
            employed = occupation != 'Unemployed'
            wealth_class = np.random.choice(list(Class), p=[0.05, 0.2, 0.2, 0.34, 0.15, 0.05, 0.01])
            
            if age >= 26:
                married = random.choice([True, False])
            else:
                married = False

            num_children = random.randint(0, 5)
            num_living_relatives = random.randint(0, 15)
            actively_breaking_law = random.random() < 0.1

            person = Person(name, age, gender, weight, education_level, occupation, is_doctor, employed, wealth_class, married, num_children, num_living_relatives, actively_breaking_law)

            people.append(person)

        return people

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Age: {self.age}\n" \
               f"Gender: {self.gender}\n" \
               f"Weight: {self.weight} lbs\n" \
               f"Education Level: {self.education_level}\n" \
               f"Occupation: {self.occupation}\n" \
               f"Is Doctor: {self.is_doctor}\n" \
               f"Employed: {self.employed}\n" \
               f"Wealth Class: {self.wealth_class.name}\n" \
               f"Married: {self.married}\n" \
               f"Number of Children: {self.num_children}\n" \
               f"Number of Living Relatives: {self.num_living_relatives}\n" \
               f"Actively Breaking Law: {self.actively_breaking_law}"

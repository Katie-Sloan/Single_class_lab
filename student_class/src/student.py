class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort

    def talk(self):
        return ("I can talk!")

    def say_favourite_language(self, language):
        return ("My favourite language is " + language)


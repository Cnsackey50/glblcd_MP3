import datetime

class Person(object):
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")

    def speak(self):
        print("Hello!")

    def walk(self):
        print("Walking away...")

    def get_name(self):
        return self.name

    def get_age(self):
        today = datetime.date.today()

        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

        return age
person()

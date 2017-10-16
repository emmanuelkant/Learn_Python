import datetime
class Person:
    def __init__(self,  name, birthday):
        self.name = name
        self.birthday = birthday

    def age(self):
        delta = datetime.date.today() -self.birthday
        return int(delta.days/365)

    def __str__(self):
        return "{0}, {1}, years old!".format(self.name, self.age())

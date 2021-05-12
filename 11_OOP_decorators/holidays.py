import datetime
import holidays

class Student:
    min_avg = 4.5
    university = 'New York Academy'

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    def email(self):
        return '{}.{}.university.com'.format(self.name, self.last)

    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Odmowa przyznania stypendium')

    @classmethod
    def set_min_avg(cls, average):
        cls.min_avg = average

    @staticmethod
    def academic_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return 'Nie'
        else:
            return 'Tak'



today = datetime.date.today()
print(today, 'zajęcia się odbywają:', Student.academic_day(today))

saturday = datetime.datetime.strptime('2019-06-22', '%Y-%m-%d')
print(saturday, 'zajęcia się odbywają:', Student.academic_day(saturday))

sunday = datetime.date.today() - datetime.timedelta(days=1)
print(sunday, 'zajęcia się odbywają:', Student.academic_day(sunday))
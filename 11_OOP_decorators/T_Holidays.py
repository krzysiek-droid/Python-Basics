import holidays
import datetime


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
    def set_avg(cls, new_avg):
        cls.min_avg = new_avg

    @staticmethod
    def academic_day(day):
        pl_holidays = holidays.Polish()
        if day in pl_holidays:
            return f"Today is a holiday day of {pl_holidays.get(day)}"
        else:
            if day.weekday() == 5 or day.weekday() == 6:
                return "Yeah, today is a weekend!"
            else:
                return "Nope, no leisure today."


today = datetime.date.today()
print(today)
print(Student.academic_day(today))

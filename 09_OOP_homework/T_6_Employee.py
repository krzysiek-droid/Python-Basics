class Employee:
    name: str
    surname: str
    position: str
    experience: str
    salary: float

    def salary_raise(self, percentage):
        self.salary *= (1 + percentage/100)

    def contributon(self):

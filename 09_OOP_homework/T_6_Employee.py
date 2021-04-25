def e_mail_generator(name, surname):
    vowels = ['a', 'e', 'u', 'o', 'y', 'i']
    address = name + surname
    for letter in address:
        if letter in vowels:
            address = address.replace(letter, '')
    return address.lower()


def tax_healthcare_cut(salary_gross, student):
    salary_net = float
    if salary_gross < 7127.33:
        salary_net = salary_gross * 0.83
    else:
        salary_net = salary_gross * 0.68
    if not student:
        salary_net -= 381.81
    return salary_net


class Employee:
    # Class general attributes
    company = "Deki"

    # Initiator attributes
    def __init__(self, name, surname, position, experience, salary_gross, student):
        self.name: str = name.capitalize()
        self.surname: str = surname.capitalize()
        self.position: str = position.capitalize()
        self.experience: int = experience
        self.salary: float = salary_gross
        self.student: bool = student
        self.salary_net: float = tax_healthcare_cut(salary_gross, student)
        self.e_mail: str = e_mail_generator(name, surname) + f'@{self.company.lower()}.com'

    # Employee methods definition
    def tax_healthcare_cut(self):
        if self.salary < 7127.33:
            self.salary_net = self.salary * 0.83
        else:
            self.salary_net = self.salary * 0.68
        if not self.student:
            self.salary_net -= 381.81

    def salary_raise(self, percentage):
        self.salary *= (1 + percentage / 100)


if __name__ == "__main__":
    Jan_Kowalski = Employee("Jan", "Kowalski", "Engineer", 5, 9250, False)
    Aleksander_Wielki = Employee("Aleksander", "Wielki", "Junior Engineer", 2, 5000, True)
    print(f'Employee: {Jan_Kowalski.name} {Jan_Kowalski.surname}| Net salary: {Jan_Kowalski.salary_net}, '
          f'e-mail: {Jan_Kowalski.e_mail}')
    print(
        f'Employee: {Aleksander_Wielki.name} {Aleksander_Wielki.surname}| Net salary: {Aleksander_Wielki.salary_net}, '
        f'e-mail: {Aleksander_Wielki.e_mail}')

import datetime

class Customer:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email


    def registration(self):
        date = datetime.date.today()
        print(date + datetime.timedelta(len(self.name) + len(self.surname)))



if __name__ == "__main__":
    kf = Customer('Krzysztof', 'Fryzowicz', 'afdsfa@gmail.com')

    kf.registration()
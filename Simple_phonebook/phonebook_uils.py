class Phonebook:
    def __init__(self, first_name, last_name, number, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.mail = mail

    def __str__(self):
        return f'{self.first_name} {self.last_name}. Number: {self.number}, email: {self.mail}\n'

    def save_new_user(self):
        with open('phonebook_vault.txt', 'a') as file:
            file.write(self.__str__())


user_1 = Phonebook('Valentin', 'Markov', '0889015360', 'markov306@gmail.com')
user_2 = Phonebook('Hans', 'Solo', '2334556', 'solo@gmail.com')

user_1.save_new_user()
user_2.save_new_user()

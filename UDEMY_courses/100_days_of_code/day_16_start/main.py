from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')
timmy.speed(1)
timmy.forward(200)
timmy.left(45)
timmy.forward(200)
timmy.left(67)
my_screen = Screen()
my_screen.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
# lst = ['Pikachu', 'Squirtle', 'Charmander']
# lst_2 = ['Electric', 'Water', 'Fire']
# table.add_column('Pokemon Name', lst)
# table.add_column('Type', lst_2)
# table.align = "r"
# print(table)

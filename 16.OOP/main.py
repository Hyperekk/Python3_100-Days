# import turtle
# bob = turtle.Turtle()
# bob.shape("turtle")
# bob.color("BlueViolet")
# bob.fd(100)
# my_screen = turtle.Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Chespin","Fennekin","Froakie"])
table.add_column("Type",["Grass","Fire","Water"])
table.align = "l"
print(table)


#      car         speed        
#object ^, attribute ^


# car.stop()
#object, method


#from turtle import Turtle, Screen
#
#johnny = Turtle()
#print(johnny)
#
#johnny.shape("turtle")
#johnny.color("black", "DarkGreen")
#
#johnny.forward(100)
#
#
#my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick() #Will only exit when terminated or a click on the screen


from prettytable import PrettyTable
table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander",]) 
table.add_column("Type", ["Electric", "Water", "Fire",])

table.align = "l"

print(table)

import turtle, random
from figures import Figure, Dynamic_figure, Colorful_figure, DynCol_Figure 

list_of_colors = ["red", "green", "yellow", "purple", "blue","pink", "black"]
cur_speed = int(input("Введите скорость черепахи от 0 до 10: "))

while cur_speed not in range(0, 11):
    print("Значение скорости черепашки должно быть от 0 до 10 (включительно)!!!")
    cur_speed = int(input("Введите скорость черепахи от 0 до 10: "))
else:
    figure = DynCol_Figure(color="green",width=2,angle=40,size=100,diff=5,
                        colors=list_of_colors,speed=cur_speed)
    figure.render(50)

#ДЗ - разработать:
# 1. Унаследовать от динамической фигуры (скрестить 2 класса)
# 2. Создать фигуру, которую можно контролировать скорость
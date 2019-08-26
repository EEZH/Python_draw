import turtle, random
from figures import Figure, Dynamic_figure, Colorful_figure, DynCol_Figure 

figure = DynCol_Figure(color="green",width=2,angle=55,size=100,diff=5,colors=["red", "green", "yellow", "purple", "blue","pink", "black"],speed=int(input("Введите скорость черепахи от 0 до 10: ")))
figure.render(50)
#["red", "green", "yellow", "purple", "blue"]
#ДЗ - разработать:
# 1. Унаследовать от динамической фигуры (скрестить 2 класса)
# 2. Создать фигуру, которую можно контролировать скорость
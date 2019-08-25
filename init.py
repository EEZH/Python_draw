import turtle
from figures import Figure, Dynamic_figure, Colorful_figure

figure = Colorful_figure(color="green",width=3,angle=85,size=100,colors=["red", "green", "yellow", "purple", "blue"])
figure.render(50)
#["red", "green", "yellow", "purple", "blue"]
#ДЗ - разработать:
# 1. Унаследовать от динамической фигуры (скрестить 2 класса)
# 2. Создать фигуру, которую можно контролировать скорость
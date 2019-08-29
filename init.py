import turtle, random
from figures import Figure, Dynamic_figure, Colorful_figure, DynCol_Figure 

list_of_colors = ["red", "green", "yellow", "purple", "blue","pink", "black"]

figure = DynCol_Figure(color="green",width=2,angle=40,size=100,diff=5,
                            colors=list_of_colors)
figure.render(50)
    


#ДЗ - разработать:
# 1. Унаследовать от динамической фигуры (скрестить 2 класса)
# 2. Создать фигуру, которую можно контролировать скорость
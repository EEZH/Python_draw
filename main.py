from classes import Controller, Device, Arduin, Raspberry

from exemple_tuple import uim

raspberry = Raspberry()

device = Device(625000, uim)

device.start_press()
device.increase_pressure(5)
device.decrease_pressure(5)
device.stop_press()


# class Ninja(Snake):
#     def __init__(self, length):
#         super().__init__(length)

# snake = Snake(100)
# ninja = Ninja(1000)
# # print(snake.hiss())
# # print(snake.crawl())
# print(snake.detect_enemy(ninja))




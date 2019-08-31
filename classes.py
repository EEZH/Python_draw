class Snake:
    def __init__(self, length):
        self.__length = length
        self.__position = 0


    def crawl(self):
        self.__position += 10
        return self.__position

    def hiss(self):
        print("ssss...")

    def detect_enemy(self, snake):
        try:
            snake.crawl()
            snake.hiss()

            print("Ok :)")
            return False

        except:
            print("SSSSS!!! >.<")
            return True

    @property
    def position(self):
        return self.__position

    @property
    def length(self):
        return self.__length

# snake = Snake(100)
# print(snake.crawl())
# print(snake.hiss())
# print(snake.detect_enemy("dfgg"))


class Controller:
    def start(self):
        pass
    
    def move_right(self, velocity):
        pass

    def move_left(self, velocity):
        pass

    def stop(self):
        pass


class Arduin(Controller):
    def start(self):
        print("Arduino start")

    def move_right(self, velocity):
        print(f"Arduino right: {velocity}")

    def move_left(self, velocity):
        print(f"Arduino left: {velocity}")

    def stop(self):
        print("Arduino stop")


class Raspberry(Controller):
    def start(self):
        print("Raspberry start")

    def move_right(self, velocity):
        print(f"Raspberry right: {velocity}")

    def move_left(self, velocity):
        print(f"Raspberry left: {velocity}")

    def stop(self):
        print("Raspberry stop")


class Device:
    def __init__(self, serial, press):
        self.serial = serial
        self.press = press

    def start_press(self):
        self.press.start()

    def increase_pressure(self, velocity):
        self.press.move_right(velocity)

    def decrease_pressure(self, velocity):
        self.press.move_left(velocity)

    def stop_press(self):
        self.press.stop()



# ДЗ:
# 1. создать класс Энимад с полями. Унаследовать кошечек, собачек и птичек
# 2. Создать класс СТартовая площадка. Создаем классы транспорта и запускаем виды транспорта с разной реализацией. 
# 3. создать транспорт от именнованного кортежа.

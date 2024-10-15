from threading import Thread
from time import sleep
import requests


class Knight(Thread):

    def __init__(self, name, power):
        self.Knight_name = name
        self.power = power
        super().__init__()

    def run(self):
        print(f"{self.Knight_name}, на нас напали!")
        enemies = 100
        days = 0
        while enemies > 0:
            sleep(1)
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f"{self.Knight_name} сражается {days} день(дня), осталось {enemies} воинов.")
        print(f"{self.Knight_name} одержал победу спустя {days}дней!")

def main():
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print("Все битвы закончились!")

if __name__ == '__main__':
    main()





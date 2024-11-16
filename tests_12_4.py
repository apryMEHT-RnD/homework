class Runner:
    def __init__(self, name, speed):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        self.name = name
        self.speed = speed
        self.distance = 0

    def walk(self):
        self.distance += self.speed * 0.5

    def run(self):
        self.distance += self.speed

    def __eq__(self, other):
        return self.name == other.name


import unittest
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8'
)


class RunnerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_walk(self):
        try:
            runner = Runner("Test Runner", -5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(123, 10)  # Неверный тип для имени
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")


# Запуск тестов
if __name__ == '__main__':
    unittest.main()
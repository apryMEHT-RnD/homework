import unittest
import module_12_2


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.hussein = module_12_2.Runner('Усейн', 10)
        self.andrey = module_12_2.Runner('Андрей', 9)
        self.nick = module_12_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({place: str(runner) for place, runner in result.items()})


    def test_start_1(self):
        race = module_12_2.Tournament(90, self.hussein, self.nick)
        results = race.start()
        self.all_results[1] = results
        runners = list(results.values())
        self.assertTrue(runners[-1] == self.nick)

    def test_start_2(self):
        race = module_12_2.Tournament(90, self.andrey, self.nick)
        results = race.start()
        self.all_results[2] = results
        runners = list(results.values())
        self.assertTrue(runners[-1] == self.nick)

    def test_start_3(self):
        race = module_12_2.Tournament(90, self.hussein, self.andrey, self.nick)
        results = race.start()
        self.all_results[3] = results
        runners = list(results.values())
        self.assertTrue(runners[-1] == self.nick)


if __name__ == '__main__':
    unittest.main()
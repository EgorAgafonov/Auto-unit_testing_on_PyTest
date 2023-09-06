"""Модуль с классом TestCalc и тестовыми функциями для unit-тестирования приложения (класса) Calculator."""
import pytest
import time
from calc import Calculator


class TestCalc:

    def setup(self):
        self.calc = Calculator
        self.start_test = time.time()

    def test_multiply_success(self):
        assert Calculator.multiply(self, 2, 2) == 4

    def test_multiply_unsuccess(self):
        assert Calculator.multiply(self, 2, 2) == 4

    def test_adding_success(self):
        assert Calculator.adding(self, 2, 2) == 4

    def test_subtraction_success(self):
        assert Calculator.subtraction(self, 2, 2) == 0

    def test_division_success(self):
        assert Calculator.division(self, 2, 2) == 1

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        self.end_test = time.time()
        filename = 'test_calculator_log.txt'
        lead_time = self.end_test - self.start_test
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f'\nДата выполнения теста: {time.asctime()}'
                    f'\nВремя выполнения коллекции тестов: {round(lead_time, 4)} сек.\n')




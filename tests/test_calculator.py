"""Модуль с классом TestCalc и тестовыми функциями для unit-тестирования приложения (класса) Calculator."""
import pytest
import time

from calc import Calculator

class TestCalc:

    def setup_class(self):
        self.calc = Calculator
        self.start_test = time.time()

    def test_multiply_success(self):
        assert Calculator.multiply(self, 2, 2) == 4

    def test_multiply_unsuccess(self):
        """Негативный тест на проверку некорректного результата при умножении чисел. Намеренно указано
        значение произведения чисел. В случае если pytest-тест не вызывает исключения AssertionError - тест не пройден,
        функция работает не корректно. А если вызов указанного исключения во время выполнения теста ("под капотом")
        происходит - тест пройден, функция работает корректно, намеренно неверно указанное значение произведения чисел
        (ожидаемый результат) действительно не соответствует фактическому(верному) результату."""

        with pytest.raises(AssertionError):
            assert Calculator.multiply(self, 8, 8) == 63

    def test_adding_success(self):
        assert Calculator.adding(self, 2, 2) == 5

    def test_subtraction_success(self):
        assert Calculator.subtraction(self, 2, 2) == 0

    def test_division_success(self):
        assert Calculator.division(self, 2, 2) == 1.0

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        self.end_test = time.time()
        filename = 'test_calculator_log.txt'
        lead_time = self.end_test - self.start_test
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f'\nДата выполнения теста: {time.asctime()}'
                    f'\nВремя выполнения коллекции тестов: {round(lead_time, 2)} сек.\n')

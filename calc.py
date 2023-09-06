""" Модуль с классом Calculator."""

class Calculator:
    """Класс Calculator с функциями сложения, вычитания, умножения и деления чисел."""

    def multiply(self, x, y):
        """Метод multiply принимает два аргумента - множимое число и множитель числа. Находит произведение
        указанных чисел и возвращает его при вызове метода."""
        return x * y

    def division(self, x, y):
        return x / y

    def subtraction(self, x, y):
        return x - y

    def adding(self, x, y):
        return x + y
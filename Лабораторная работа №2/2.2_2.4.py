import logging
import unittest

def log_calculation(func):
    def wrapper(x, y, action):
        # Логируем перед вызовом функции
        logging.info(f"Calculating: {action} with operands {x} and {y}")
        result = func(x, y, action)  # Вызов основной функции с передачей action
        # Логируем после выполнения
        logging.info(f"Result: {result}")
        return result
    return wrapper

@log_calculation
def calculate(x, y, action):
    if action == '1':  # Сложение
        return addition(x, y)
    elif action == '2':  # Вычитание
        return subtraction(x, y)
    elif action == '3':  # Умножение
        return multiplication(x, y)
    elif action == '4':  # Деление
        return division(x, y)
    else:
        return "Invalid action!"

def addition(x, y):  # Исправлено: "addittion" на "addition"
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error!"
    return x / y

def calculator():
    while True:
        choice = input("Enter choice:\n   1. Addition \n   2. Subtraction \n   3. Multiplication \n   4. Division \n")
        if choice in ('1', '2', '3', '4'):
            try:
                number_1 = float(input("Enter first number: "))
                number_2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue
            result = calculate(number_1, number_2, choice)
            print(f"Result: {result}")
            if input("Do you want to perform another operation? (Dial 'no' to exit): ") == "no":
                break
        else:
            print("Error! This number is not from the list. Please enter the transaction number.")


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(1, 1), 2)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(-1, -1), -2)

    def test_subtraction(self):
        self.assertEqual(subtraction(1, 1), 0)
        self.assertEqual(subtraction(5, 2), 3)
        self.assertEqual(subtraction(-1, 1), -2)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(0, 5), 0)
        self.assertEqual(multiplication(-2, 4), -8)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertEqual(division(0, 5), 0)
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(4, 0), "Error!")


if __name__ == "__main__":
    unittest.main()
    #calculator()

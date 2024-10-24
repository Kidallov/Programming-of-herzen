import logging
import math

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_precision(tolerance):
    """Convert tolerance to the number of decimal places."""
    return abs(int(round(math.log10(tolerance))))

def log_calculation(func):
    """Decorator to log calculations."""
    def wrapper(action, *numbers, tolerance=1e-6):
        logging.info(f"Calculating: {' '.join(map(str, numbers))} {action}")
        result = func(action, *numbers, tolerance=tolerance)
        logging.info(f"Result: {result}")
        return result
    return wrapper

@log_calculation
def calculate(action, *numbers, tolerance=1e-6):
    """Perform a calculation based on the action provided."""
    if not numbers:
        return "No numbers provided!"

    operations = {
        '+': lambda *args: sum(args),
        '-': lambda *args: args[0] - sum(args[1:]),
        '*': lambda *args: math.prod(args),
        '/': lambda *args: "Error: Division by zero!" if 0 in args[1:] else args[0] / math.prod(args[1:])
    }

    func = operations.get(action)
    if func:
        result = func(*numbers)

        return round(result, convert_precision(tolerance)) if isinstance(result, (int, float)) else result
    else:
        return "Invalid action!"

def calculator(action, *numbers):
    """Main calculator function that accepts multiple numbers with a single operator."""
    result = calculate(action, *numbers)
    print(f"Result: {result}")

if __name__ == "__main__":

    calculator()

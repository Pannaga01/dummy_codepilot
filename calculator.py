def calculate(num1, operator, num2=None):
    if operator in ['+', '-', '*', '/'] and num2 is None:
        return "Error: Missing second operand for this operator"
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    elif operator == '^2':
        if num2 is not None:
            return "Error: Unary operator '^2' does not accept a second operand"
        return num1 ** 2
    else:
        return "Error: Invalid operator"

if __name__ == "__main__":
    print(f"5 + 3 = {calculate(5, '+', 3)}")
    print(f"10 - 4 = {calculate(10, '-', 4)}")
    print(f"6 * 7 = {calculate(6, '*', 7)}")
    print(f"10 / 2 = {calculate(10, '/', 2)}")
    print(f"7 ^ 2 = {calculate(7, '^2')}")
    print(f"7 ^ 2 with num2 = {calculate(7, '^2', 3)}") # Test case for unary operator with num2
    print(f"10 / 0 = {calculate(10, '/', 0)}")
    print(f"5 % 2 = {calculate(5, '%', 2)}")
    print(f"5 + = {calculate(5, '+')}") # Test case for missing num2

ef calculate(num1, operator, num2=None):
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
        return num1 ** 2
    else:
        return "Error: Invalid operator"

if __name__ == "__main__":
    print(f"5 + 3 = {calculate(5, '+', 3)}")
    print(f"10 - 4 = {calculate(10, '-', 4)}")
    print(f"6 * 7 = {calculate(6, '*', 7)}")
    print(f"10 / 2 = {calculate(10, '/', 2)}")
    print(f"7 ^ 2 = {calculate(7, '^2')}")
    print(f"10 / 0 = {calculate(10, '/', 0)}")
    print(f"5 % 2 = {calculate(5, '%', 2)}")

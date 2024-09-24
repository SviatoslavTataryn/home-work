from variables import translator, language, is_start, VR_PLUS, VR_MINUS, VR_MULTIPLY, VR_DIVIDE


def greeting():
    while True:
        language = input("Hello, choose language (ukr or eng) -> ").strip()
        if language in translator:
            break
        else:
            print("Invalid language choice. Please select 'ukr' or 'eng'.")


def input_number(name) -> float:
    while True:
        try:
            return float(input(translator[language][name]))
        except ValueError:
            print(translator[language]["Invalid input number"])


def input_operation():
    list_operators = [VR_PLUS, VR_MINUS, VR_MULTIPLY, VR_DIVIDE]
    while True:
        operator = input(translator[language]["operator"]).strip()
        if operator in list_operators:
            return operator
        else:
            print(f"({operator}) {translator[language]['Invalid input operator']}")


def operation(first_number, second_number, operator):
    if operator == VR_PLUS:
        result = first_number + second_number
    elif operator == VR_MINUS:
        result = first_number - second_number
    elif operator == VR_MULTIPLY:
        result = first_number * second_number
    elif operator == VR_DIVIDE:
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Error: Division by zero"
    print(translator[language]["result"], result)


def start_calculator():
    while is_start:
        first_number = input_number("first number")
        operator = input_operation()
        second_number = input_number("second number")

        operation(first_number, second_number, operator)

        is_end = input(translator[language]["repeat"]).strip().lower()
        if is_end == "n":
            is_start = False


def main():
    greeting()
    start_calculator()


main()

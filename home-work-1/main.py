from variables import translator, is_start, result, operator, first_number, second_number, VR_PLUS, VR_MINUS, VR_MULTIPLY, VR_DIVIDE

while True:
    language = input("Hello, choose language (ukr or eng) -> ").strip()
    if language in translator:
        break
    else:
        print("Invalid language choice. Please select 'ukr' or 'eng'.")

while is_start:
    try:
        first_number = float(input(translator[language]["first number"]))
    except ValueError:
        print(translator[language]["Invalid input number"])
        continue

    list_operators = [VR_PLUS, VR_MINUS, VR_MULTIPLY, VR_DIVIDE]

    while True:
        operator = input(translator[language]["operator"]).strip()
        if operator in list_operators:
            break
        else:
            print(f"({operator}) {translator[language]['Invalid input operator']}")

    try:
        second_number = float(input(translator[language]["second number"]))
    except ValueError:
        print(translator[language]["Invalid input number"])
        continue

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

    is_end = input(translator[language]["repeat"]).strip().lower()
    if is_end == "n":
        is_start = False

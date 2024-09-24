# ... Напиши функцію multiply(), яка приймає будь-яку кількість числових аргументів і повертає їх добуток. multiply(1, 2, 3, 4);  // 24

# Напиши функцію filter_even_numbers(arr), яка повертає новий масив, що містить тільки парні числа з масиву arr. filterEvenNumbers([1, 2, 3, 4, 5, 6]);  // [2, 4, 6]

def multiply(*args) -> int:
    result = []
    for n in args:
        result += n
    return result


list_num = [16]
list_num2 = [16]
print(multiply(list_num, list_num2))


def filter_even_numbers(numbers) -> list:
    num_list = []
    for n in numbers:
        if n % 2 == 0:
            num_list.append(n)
    return num_list

print(filter_even_numbers([1,2,3,4,5,]))
class Multiply:

    # 3. Створи функцію multiplyByTwo(arr),
    # яка приймає масив чисел і повертає новий масив, у якому кожен елемент помножено на 2.

    def multiplyByTwo(self, list_numbers) -> list:
        new_list = []
        for i in list_numbers:
           new_list.append(i * 2)
        return new_list

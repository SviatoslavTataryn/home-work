class Sum:

    # 2. Реалізуй функцію sumNestedArray(arr),
    # яка обчислює суму всіх чисел у масиві.

    def sumNestedArray(self, list_numbers :list) -> float:
        sum = 0
        for i in list_numbers:
            sum += i
        return sum


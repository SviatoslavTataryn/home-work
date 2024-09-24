from sort_dates import Dates
from longest_word import Finder
from sum_numbers import Sum
from multiply import Multiply
from max_value import MaxValue
from even_number import EvenNumber

if __name__ == "__main__":
    list_dates = ['2024-01-01', '2023-05-15', '2024-08-12']
    string = "It is a sentence with a very long word"
    list_numbers = [1,2,3,4,5,6,7,8]
    not_event_number = 7
    event_number = 10

    dates = Dates()
    finder = Finder()
    sum = Sum()
    multiply = Multiply()
    max_value = MaxValue()
    event_num = EvenNumber()

    print(dates.sortDates(list_dates))
    print(finder.findLongestWord(string))
    print(sum.sumNestedArray(list_numbers))
    print(multiply.multiplyByTwo(list_numbers))
    print(max_value.findMax(list_numbers))
    print(event_num.isEven(not_event_number))
    print(event_num.isEven(event_number))

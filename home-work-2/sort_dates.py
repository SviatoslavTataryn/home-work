from datetime import datetime

# Напиши функцію sortDates(dates),
# яка сортує масив дат у порядку зростання.
# sortDates(['2024-01-01', '2023-05-15', '2024-08-12']);

class Dates:
    FORMAT_DATA = "%Y-%m-%d"

    @staticmethod
    def __convert_to_object(dates: list) -> list:
        return [datetime.strptime(date, Dates.FORMAT_DATA) for date in dates]

    @staticmethod
    def __convert_to_string(dates_obj: list) -> list:
        return [datetime.strftime(date, Dates.FORMAT_DATA) for date in dates_obj]

    def sortDates(self, dates: list) -> list:
        dates_obj = Dates.__convert_to_object(dates)
        sorted_list_objects = sorted(dates_obj)
        return Dates.__convert_to_string(sorted_list_objects)



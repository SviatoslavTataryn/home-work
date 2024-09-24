class Finder:

    # 1. Створи функцію findLongestWord(str),
    # яка приймає рядок str і повертає найдовше слово у цьому рядку.
    # Якщо є кілька слів однакової довжини, повернути перше.

    def findLongestWord(seft, string: str) -> str:
        return max(string.split(), key=len)

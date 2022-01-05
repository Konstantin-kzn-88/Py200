# Создать класс Date.
#
# Класс должен содержать конструктор (__init__).
# В конструкторе должны быть объявлены 3 атрибута: день месяц год
#
# При инициализации должны быть проверки только TypeError, на проверку соответствия целочисленным значениям.
# Проверки типа, что в месяце не может быть больше 31 дня, плюс не для каждого месяца, ... на данном этапе опускаем.
#
# В классе должны быть магические методы __repr__ и __str__.
# Метод __repr__ должен возвращать такую строку, по которой может быть создан эквивалентный экземпляр.
# Метод __str__ должен возвращать строку формата
#
# DD/MM/YYYY
# где DD - день, MM - месяц, YYYY - год.
#
# Например:
#
# 01/01/2021
# 11/10/1999
#
# 1/1/2021 - неверно

class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = self.__check_day(day)
        self.month = self.__check_month(month)
        self.year = self.__check_year(year)

    def __repr__(self) -> str:
        return f"Date({self.day}, {self.month}, {self.year})"

    def __str__(self) -> str:
        if len(str(self.day)) == 1:
            day = "0" + str(self.day)
        else:
            day = str(self.day)

        if len(str(self.month)) == 1:
            month = "0" + str(self.month)
        else:
            month = str(self.month)
        year = str(self.year)
        return f"{day}/{month}/{year}"

    @staticmethod
    def __check_day(value):
        if not isinstance(value, int):
            raise TypeError("Не число")
        if value > 31:
            raise TypeError("Больше 31 дня")
        return value

    @staticmethod
    def __check_month(value):
        if not isinstance(value, int):
            raise TypeError("Не число")
        if value > 12:
            raise TypeError("Больше 12 месяцев")
        return value

    @staticmethod
    def __check_year(value):
        if not isinstance(value, int):
            raise TypeError("Не число")
        if value < 1000:
            raise TypeError("Число должно быть больше 1000")
        return value

if __name__ == "__main__":
    date = Date(1,1,1988)
    print(date.__repr__())
    print(date.__str__())

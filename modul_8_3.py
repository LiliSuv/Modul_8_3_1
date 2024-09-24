class IncorrectVinNumber (Exception):
    def __init__(self, message):
        self.message = message
        print (self.message)


class IncorrectCarNumbers (Exception):
    def __init__(self, message):
        self.message = message
        print (self.message)


class Car:
    def __init__(self, model, __vin, __numbers):
        self.vin = __vin
        self.model = model
        self.numbers = __numbers
        if self.__is_valid_vin (self.vin) == True and self.__is_valid_numbers (self.numbers) == True:
            print (f'{self.model} успешно создан\n', ('_' * 40))

    def get__vin(self):
        return self.vin

    def get__numbers(self):
        return self.numbers

    def __is_valid_vin(self, vin):
        try:
            if not isinstance (vin, int):
                raise IncorrectVinNumber (f'{self.model} Некорректный тип vin номерa')
            if not 1000000 <= vin <= 9999999:
                raise IncorrectVinNumber (f'{self.model} Неверный диапазон для vin номера')
        except IncorrectVinNumber:
            print ('_' * 40)

        else:
            return True

    def __is_valid_numbers(self, numbers):
        try:
            if not isinstance (numbers, str):
                raise IncorrectCarNumbers (f'{self.model} Некорректный тип данных для номеров')
            if len (numbers) != 6:
                raise IncorrectCarNumbers (f'{self.model} Неверная длина номера')
        except IncorrectCarNumbers:
            print ('_' * 40)
        else:
            return True


Car ('Model1', 1000000, 'f123dj')
Car ('Model2', 300, 'т001тр')
Car ('Model3', 10000.00, 'f123dj')
Car ('Model4', 20000000, 'т001тр')
Car ('Model5', 2020202, 'нет номера')
Car ('Model6', 2000000, '{т0:01тр}')

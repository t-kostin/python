# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут
# должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса
# Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:

    def __init__(self, arg_nm, arg_sur, arg_pos, arg_wg, arg_bon):
        self.name = arg_nm
        self.surname = arg_sur
        self.position = arg_pos
        self._income = dict(wage=arg_wg, bonus=arg_bon)


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


staff = Position('John', 'Doe', 'manager', 1000, 2000)
print(f'Full name: {staff.get_full_name()}; Total income: ${staff.get_total_income()}.')

# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
# width (ширина). Значения данных атрибутов должны передаваться при создании
# экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина × ширина × масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см × число см толщины полотна. Проверить работу метода.


class Road:

    def __init__(self, arg_ln, arg_wd):
        self._length = arg_ln
        self._width = arg_wd

    def mass(self, arg_mass_per_sq, arg_thickness):
        return self._width * self._length * arg_mass_per_sq * arg_thickness


avenue = Road(5000, 9)
asphalt_mass = avenue.mass(25, 7)
print(asphalt_mass)

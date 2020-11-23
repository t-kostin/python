# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
# к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, arg_nm: str, arg_col: str, arg_spd: int, arg_pol=False):
        self.name = arg_nm
        self.color = arg_col
        self.speed = arg_spd
        self.is_police = arg_pol

    def go(self):
        print(self.name, 'поехал.')

    def stop(self):
        print(self.name, 'остановился.')

    def turn(self, arg_direction):
        print(f'{self.name} повернул {arg_direction}.')

    def show_speed(self):
        print(f'Скорость {self.name} составляет {self.speed} км/ч.')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            speeding = ' Превышение скорости!'
        else:
            speeding = ''
        print(f'Скорость {self.name} составляет {self.speed} км/ч.{speeding}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            speeding = ' Превышение скорости!'
        else:
            speeding = ''
        print(f'Скорость {self.name} составляет {self.speed} км/ч.{speeding}')

class PoliceCar(Car):
    pass


car1 = Car('Опель', 'черный', 90)
car2 = TownCar('Митсубиси', 'синий', 60)
car3 = WorkCar('Фольксваген', 'серебристый', 70)
car4 = SportCar('МакЛарен', 'красный', 100)
car5 = PoliceCar('Форд', 'белый', 80, True)

print(car1.name, car1.color, car1.speed, car1.is_police)
print(car2.name, car2.color, car2.speed, car2.is_police)
print(car3.name, car3.color, car3.speed, car3.is_police)
print(car4.name, car4.color, car4.speed, car4.is_police)
print(car5.name, car5.color, car5.speed, car5.is_police)
print('=' * 30)
car1.go()
car1.turn('налево')
car1.stop()
print('=' * 30)
car3.go()
car3.turn('направо')
car3.stop()
print('=' * 30)
car2.show_speed()
car3.show_speed()
car4.show_speed()
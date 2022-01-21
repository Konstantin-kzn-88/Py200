from car import Car
from driver import Driver


def beautiful_print(block_name):
    print(end='\n\n\n')
    print('=' * 60)
    print(block_name)
    print('=' * 60, end='\n\n')


def block_1_class_attributes():

    red_sedan = Car('красный', 'седан')
    print('Создаём', repr(red_sedan))
    print(red_sedan)
    print(f'{red_sedan} Колёс {red_sedan.wheel_count}. Тип двигателя {red_sedan._engine_type}', end='\n\n')
    # red_sedan.wheel_count можем получить значение
    # red_sedan._engine_type можем получить значение, но разработчик захотел скрыть это

    blue_coupe = Car('синий', 'купе')
    print('Создаём', repr(blue_coupe))
    print(blue_coupe)
    print(f'{blue_coupe} Колёс {blue_coupe.wheel_count}. Тип двигателя {blue_coupe._engine_type}', end='\n\n')

    print('Добавили колесо и поменяли тип двигателя')
    Car.wheel_count = 5
    Car._engine_type = 'электрический'

    print(f'{red_sedan} Колёс {red_sedan.wheel_count}. Тип двигателя {red_sedan._engine_type}', end='\n\n')
    print(f'{blue_coupe} Колёс {blue_coupe.wheel_count}. Тип двигателя {blue_coupe._engine_type}', end='\n\n')

    print(f'Все атрибуты класса Car для {repr(red_sedan)}\n', dir(red_sedan), end='\n\n')
    print(f'Все атрибуты класса Car для {repr(blue_coupe)}\n', dir(blue_coupe), end='\n\n')


def block_2_instance_attribute():
    black_cabrio = Car('чёрный', 'кабриолет')
    print('Создаём', repr(black_cabrio))
    print(f'{black_cabrio} Колёс {black_cabrio.wheel_count}. Тип двигателя {black_cabrio._engine_type}', end='\n\n')

    green_hatch = Car('зелёный', 'хэтчбек')
    print('Создаём', repr(green_hatch))
    print(f'{green_hatch} Колёс {green_hatch.wheel_count}. Тип двигателя {green_hatch._engine_type}', end='\n\n')

    print('Меняем цвет и садим водителя')

    black_cabrio.color = 'жёлтый'
    green_hatch._driver = Driver('Вася')

    print(f'{black_cabrio} '
          f'Колёс {black_cabrio.wheel_count}. '
          f'Тип двигателя {black_cabrio._engine_type}. '
          f'Водитель {black_cabrio._driver}', end='\n\n')

    print(f'{green_hatch} '
          f'Колёс {green_hatch.wheel_count}. '
          f'Тип двигателя {green_hatch._engine_type}. '
          f'Водитель {green_hatch._driver}', end='\n\n')


def block_3_instance_methods():
    black_cabrio = Car('чёрный', 'кабриолет')
    print('Создаём', repr(black_cabrio))

    # пытаемся ехать, как только создали машину
    # black_cabrio.move()

    # пытаемся завести машину и поехать
    # black_cabrio.start_engine()
    # black_cabrio.move()

    # сажаем водителя и только тогда едем
    black_cabrio.start_engine()
    black_cabrio._driver = Driver('Стиг')
    black_cabrio.move()


def block_4_classes_methods():
    print(f"Колёс у автомобилей класса Car: {Car.get_wheel_count()}")
    print(f"Ездили машины класса Car на: {Car._engine_type}")
    Car._set_engine_type("электричество")
    print(f"Стали ездить на: {Car._engine_type}")

    [Car("чёрный", "седан") for i in range(10)]


def block_5_static_methods():
    print(Car.is_car("red", "cabrio"))


beautiful_print('БЛОК 1 - атрибуты класса')
block_1_class_attributes()

beautiful_print('БЛОК 2 - атрибуты экземпляра класса')
block_2_instance_attribute()

beautiful_print('БЛОК 3 - методы экземпляра класса')
block_3_instance_methods()

beautiful_print('БЛОК 4 - методы класса')
block_4_classes_methods()

beautiful_print('БЛОК 5 - статические методы')
block_5_static_methods()







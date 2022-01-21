from car import Car


class Honda(Car):
    def __init__(self):
        super(Honda, self).__init__("Белый", "Кроссовер")


if __name__ == '__main__':
    new_honda = Honda()

    print(new_honda.color)

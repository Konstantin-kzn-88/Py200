import matplotlib.pyplot as plt
import numpy as np

class Рarallelepiped:
    def __init__(self, x: int, y: int, z: int, color: str):
        self.__x, self.__y, self.__z = self.__check_side(x, y, z)
        self.__color = self.__check_color(color)

    @staticmethod
    def __check_side(x: int, y: int, z: int):
        if not isinstance(x, int):
            raise TypeError("Сторона х - не целое число")
        if not isinstance(y, int):
            raise TypeError("Сторона y - не целое число")
        if not isinstance(z, int):
            raise TypeError("Сторона z - не целое число")
        if x > 10:
            raise TypeError("Сторона х превышает сетку")
        if y > 10:
            raise TypeError("Сторона y превышает сетку")
        if z > 10:
            raise TypeError("Сторона z превышает сетку")
        return x, y, z

    @staticmethod
    def __check_color(color: str):
        if color not in ['b', 'r', 'c', 'm', 'y', 'k', 'w']:
            raise TypeError("Нужен цвет из 'b', 'r', 'c', 'm', 'y', 'k', 'w'")
        return color

    def __repr__(self):
        return f"Рarallelepiped({self.__x}, {self.__y}, {self.__z}, {self.__color})"

    def draw_fig(self):
        # остроим координатную сетку размеров 8 на 8 на 8 (3D)
        x_axis, y_axis, z_axis = np.indices((10, 10, 10))
        parallelepiped = (x_axis < self.__x) & (y_axis < self.__y) & (z_axis < self.__z)
        # объекты в один массив
        voxelarray = parallelepiped
        # установим цвет
        colors = np.empty(voxelarray.shape, dtype=object)
        colors[parallelepiped] = self.__color
        # отрисуем все
        ax = plt.figure().add_subplot(projection='3d')
        ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

        plt.show()

    def calc_volume(self):
        return f"V = {self.__x * self.__y * self.__z} ед."


if __name__ == "__main__":
    cube = Рarallelepiped(9, 9, 9, 'b')
    print(cube.calc_volume())
    cube.draw_fig()

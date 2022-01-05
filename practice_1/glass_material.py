# Написать класс Glass с одним атрибутом material и методом get_material,
# который его будет возвращать атрибут material.

class Glass:
    def __init__(self, material: str):
        self.__material = material

    def get_material(self) -> str:
        return self.__material


if __name__ == "__main__":
    glass_1 = Glass("steel")
    print(glass_1.get_material())

# Двусвязный список на основе односвязного списка.
#
# Односвязный список LinkedList должен быть унаследован он абстрактного типа MutableSequence из модуля collections.abc.
#
# В односвязном списке должны быть реализованы следующие методы:
#
# __get_item__
# __set_item__
# __del_item__
# __len__
# __str__
# __repr__
# insert
# append
# Все атрибуты должны быть инкапсулированы.
# То есть быть либо private или protected по вашему выбору.

# Двусвязный список DoubleLinkedList должен наследоваться от LinkedList.
# Для экземпляров данного класса должны работать все методы базового класса.
#
# Необязательно все эти методы должны быть перегружены. По максимуму используйте наследование,
# если поведение списков в контексте реализации указанных метод схоже.
# С точки зрения наследования по минимуму перегружайте методы.
# При необходимости рефакторите базовый класс, чтобы локализовать части кода во вспомогательные функции,
# которые имеют различное поведение в связном и двусвязном списках.
#
# Стремитесь к минимизации кода в дочернем классе.
# https://github.com/python/cpython/blob/208a7e957b812ad3b3733791845447677a704f3e/Lib/collections/__init__.py#L1174
# https://pythobyte.com/linked-lists-in-detail-with-python-examples-single-linked-lists-7ac94da7/

from typing import Any
from collections.abc import MutableSequence


class Node:
    """
    Класс узла
    :param _item - данные в узле (любые)
    :param _next_item - ссылка на следующий узел
    :param _previous_item - ссылка на предыдущий узел (для односвязного списка,
    во всех узлах будет None)
    """

    def __init__(self, data: Any):
        self._item = data
        self._next_item = None
        self._previous_item = None


class LinkedList(MutableSequence):
    """
    Класс односвязного списка, наследованный от MutableSequence (collections.abc)
    :param start_node - первый узел

    Значение start_node будет None, так как связанный
    список будет пуст в момент создания.
    """

    def __init__(self):
        self.start_node = None

    def make_new_list(self) -> None:
        """Функция изготовления односвязанного списка"""
        nums = int(input("Сколько узлов вы хотите сделать: "))
        if nums == 0:
            return
        for i in range(nums):
            value = input("Введите значение узла:")
            self.append(value)

    def bypass_list(self) -> None:
        """
        Функция обхода односвязного списка
        """
        if self.start_node is None:
            print("В списке нет элементов")
            return
        else:
            n = self.start_node
            while n is not None:
                print(f'_item = {n._item}, _next_item = {n._next_item}, _previous_item = {n._previous_item}')
                n = n._next_item

    def append(self, data: Any) -> None:
        """
        Функция вставки в конец связного списка
        :param data - данные узла
        """
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n._next_item is not None:
            n = n._next_item
        n._next_item = new_node

    def insert(self, element: Any, data: Any) -> None:
        """
        Функция вставки после определенного элемента
        :param data - данные узла
        :param element - элемент списка после которого следует вставить новый узел (data)
        """
        n = self.start_node
        while n is not None:
            if n._item == element:
                break
            n = n._next_item
        if n is None:
            print("Элемента нет в списке")
        else:
            new_node = Node(data)
            new_node._next_item = n._next_item
            n._next_item = new_node

    def __len__(self) -> Any:
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count = count + 1
            n = n._next_item
        return count

    def __delitem__(self, element) -> None:
        """Удаление конкретного элемента"""
        if self.start_node is None:
            print("В списке нет элемента для удаления")
            return

        if self.start_node._item == element:
            self.start_node = self.start_node._next_item
            return

        n = self.start_node
        while n._next_item is not None:
            if n._next_item._item == element:
                break
            n = n._next_item

        if n._next_item is None:
            print("Элемент не найден в в списке")
        else:
            n._next_item = n._next_item._next_item

    def __getitem__(self, num_element: int):

        if self.start_node is None:
            raise Exception("Список пуст")
        if num_element > self.__len__() - 1:
            raise Exception("Индекс больше длины списка")

        n = self.start_node
        count = 0
        while n is not None:
            if count == num_element:
                return n._item
            n = n._next_item
            count += 1

    def __setitem__(self, num_element: int, data: Any) -> None:

        if self.start_node is None:
            raise Exception("Список пуст")
        if num_element > self.__len__() - 1:
            raise Exception("Индекс больше длины списка")

        n = self.start_node
        count = 0
        while n is not None:
            if count == num_element:
                n._item = data
                return
            n = n._next_item
            count += 1

    def __repr__(self):
        return f'{self.__class__.__name__}()'


class DoubleLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def append(self, data: Any) -> None:
        """
        Функция вставки в конец связного списка
        :param data - данные узла
        """
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n._next_item is not None:
            n = n._next_item
            n._previous_item = n
        n._next_item = new_node
        new_node._previous_item = n._next_item



if __name__ == "__main__":
    # 1. Инициализируем новый список
    new_linked_list = LinkedList()
    # 2. Запустим функцию создания списка (!!! обязательно сделать узел "test_node" см. п.4)
    new_linked_list.make_new_list()
    # 3. Добавим в конец новый узел
    new_linked_list.append("Данные нового узла")
    # Распечатаем узлы
    new_linked_list.bypass_list()
    print("___Вставка___")
    print(" " * 20)
    # 4. Вставить узел "125" после "test_node"
    new_linked_list.insert("test_node", "125")
    # Распечатаем узлы
    new_linked_list.bypass_list()
    # 5. Выведем первый элемент по индексу
    print(new_linked_list[1])
    # 6. Замена данных в узле
    print("__Замена данных в узле__")
    print(" " * 20)
    new_linked_list[2] = "Заменные данные в узле"
    # Распечатаем лист
    new_linked_list.bypass_list()
    print("__Двусвязный список__")
    print(" " * 20)
    # 7. Двусвязный список унаследованный от односвязного
    new_double_linked_list = DoubleLinkedList()
    # 8. Запустим функцию создания списка (!!! обязательно сделать узел "test_node" см. п.4)
    new_double_linked_list.make_new_list()
    # Распечатаем лист
    new_double_linked_list.bypass_list()

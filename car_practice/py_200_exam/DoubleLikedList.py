# Двусвязный список на основе односвязного списка.
#
# Односвязный список LinkedList должен быть унаследован он абстрактного типа MutableSequence из модуля collections.abc.
#
# В односвязном списке должны быть реализованы следующие методы:
#
# __getitem__
# __setitem__
# __delitem__
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

from collections.abc import MutableSequence

class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList(MutableSequence):
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("В списке нет элементов")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node

    def insert_after_item(self, x, data):

        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def get_count(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count = count + 1
            n = n.ref
        return count

    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False

    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        # Deleting first node
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return

        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref

    def reverse_linkedlist(self):
        prev = None
        n = self.start_node
        while n is not None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.start_node = prev

    def make_new_list(self):
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for i in range(nums):
            value = int(input("Enter the value for the node:"))
            self.insert_at_end(value)


    def __len__(self):
        return len(self.__data)

    def __getitem__(self, i):
        if isinstance(i, slice):
            return self.__class__(self.__data[i])
        else:
            return self.__data[i]

    def __setitem__(self, i, item):
        self.__data[i] = item

    def __delitem__(self, i):
        del self.__data[i]

    def __repr__(self):
        return repr(self.__data)

    def append(self, item):
        self.__data.append(item)

    def insert(self, i, item):
        self.__data.insert(i, item)


if __name__ == "__main__":
    new_linked_list = LinkedList()
    new_linked_list.insert_at_end(5)
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(15)
    new_linked_list.traverse_list()
    new_linked_list.insert_at_start(20)
    new_linked_list.insert_after_item(10, 17)
    new_linked_list.insert_before_item(17, 25)
    new_linked_list.insert_at_index(3,8)
    new_linked_list.get_count()
    new_linked_list.search_item(5)
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(20)
    new_linked_list.insert_at_end(30)
    new_linked_list.insert_at_end(40)
    new_linked_list.insert_at_end(50)
    new_linked_list.delete_at_end()
    new_linked_list.delete_element_by_value(30)



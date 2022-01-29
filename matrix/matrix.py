class Matrix:
    def __init__(self, row: int, column: int):
        self.matrix = []
        self.row = row
        self.column = column

        # Заполнение 1
        for i in range(row):
            a = []
            for j in range(column):
                a.append(1)
            self.matrix.append(a)

    def addition_matrix(self, matrix):
        "Сложение с другой матрицей"
        original_matrix = self.matrix
        if len(matrix) != len(original_matrix):
            return
        for i in range(len(original_matrix)):
            for k in range(len(matrix)):
                self.matrix[i][k] = original_matrix[i][k] + matrix[i][k]
        self.print_matrix()

    def multiplication_matrix(self, matrix):
        "Умножение с другой матрицей"
        original_matrix = self.matrix
        if len(matrix) != len(original_matrix):
            return
        for i in range(len(original_matrix)):
            for k in range(len(matrix)):
                self.matrix[i][k] = original_matrix[i][k] * matrix[i][k]
        self.print_matrix()

    def multiplication_int(self, value: int):
        "Умножение на число"
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix)):
                self.matrix[i][k] = self.matrix[i][k] * value
        self.print_matrix()

    def print_matrix(self):
        # Распечатать в виде матрицы
        print(10 * "-")
        for i in range(self.row):
            for j in range(self.column):
                print(self.matrix[i][j], end=" ")
            print()
        print(10 * "-")

    def return_matrix(self):
        return self.matrix


if __name__ == "__main__":
    m = Matrix(3, 3)
    m2 = Matrix(3, 3)
    m.addition_matrix(m2.return_matrix())
    m.multiplication_matrix(m2.return_matrix())
    m.multiplication_int(2)

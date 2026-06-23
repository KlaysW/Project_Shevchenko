# Вариант 32.
# 1. Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
# Добавьте методы для сложения, вычитания и умножения матриц.

import random

class Matrix:
    def __init__(self, rows, cols, fill_random=True):
        self.rows = rows
        self.cols = cols
        if fill_random:
            self.data = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]
        else:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера")
        result = Matrix(self.rows, self.cols, fill_random=False)
        result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера")
        result = Matrix(self.rows, self.cols, fill_random=False)
        result.data = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
        result = Matrix(self.rows, other.cols, fill_random=False)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
        return result

matrix1 = Matrix(int(input("Введите количество строк для первой матрицы: ")), int(input("Введите количество столбцов для первой матрицы: ")))
matrix2 = Matrix(int(input("Введите количество строк для второй матрицы: ")), int(input("Введите количество столбцов для второй матрицы: ")))

print("Матрица 1:")
print(matrix1)
print("\nМатрица 2:")
print(matrix2)

print("\nРезультат сложения:")
print(matrix1.add(matrix2))

print("\nРезультат вычитания:")
print(matrix1.subtract(matrix2))

print("\nРезультат умножения:")
print(matrix1.multiply(matrix2))
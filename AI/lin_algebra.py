from typing import List

Vector = List[float]    # Аннотированный тип -> массив из !вещественных! чисел
x: int = "test"         # Аннотирование что переменная <x> будет int, но ошибки не возникнет, если это будет не так

def add(v: Vector, w: Vector) -> Vector:
    """ Сложение 2ух векторов """
    assert len(v) == len(w)     # проверка на одинаковую размерность векторов
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def substract(v: Vector, w: Vector) -> Vector:
    """ Вычитание 2ух векторов """
    assert len(v) == len(w)     # проверка на одинаковую размерность векторов
    return [v_i - w_i for v_i, w_i in zip(v, w)]

# Аргумент <vectors> : массив массивов вещественных чисел ;)
def vector_sum(vectors: List[Vector]) -> Vector:
    # Проверка что аргумент - векторы не пустой
    assert vectors, "отсутствуют векторы для сложения, [ERROR -> vector_sum()]"

    # Проверка размерностей переданных векторов
    szVectors = len(vectors[0])
    assert all(len(v) == szVectors for v in vectors), "разная размерность векторов, [ERROR -> vector_sum()]"

    # повекторное сложение
    return [sum(vector[i] for vector in vectors) for i in range(szVectors)]     # sum( vectors[0] -> 1, 3, 5, 7 ); sum( vectors[1] -> 2, 4, 6, 8 )

height_weight_age = [175, 68, 40]
grades = [95, 80, 75, 62]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
assert substract([4, 5, 6], [1, 2, 3]) == [3, 3, 3]
summ_vectors = vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]])
pass
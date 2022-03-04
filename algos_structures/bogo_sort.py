import random

# метод проверки упорядоченности массива
def is_sorted(array):
    length = len(array)
    for i in range(0, length - 1):
        if(array[i] > array[i + 1]):
            return False
    return True

# перемешивание массива в случайном порядке
def random_permutation(array):
    length = len(array)
    for i in range(0, length):
        rnd = random.randint(0, length - 1)
        # обмен элементов массива
        temp = array[i]
        array[i] = array[rnd]
        array[rnd] = temp

# случайная сортировка
def bogo_sort(array):
    while(not(is_sorted(array))):
        random_permutation(array)

print("Случайная сортировка")
arr = []
n = int(input("Введите длину массива: ")) 
for i in range(0, n): 
    element = int(input("arr[" + str(i + 1) + "] = "))   
    arr.append(element)
bogo_sort(arr) 
print("Отсортированный массив: ") 
print(arr) 
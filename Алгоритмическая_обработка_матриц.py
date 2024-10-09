"""
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N)
заполняется случайным образом целыми числами в интервале [-10,10].
Для тестирования использовать не случайное заполнение,
а целенаправленное, введенное из файла.
17. Формируется матрица F следующим образом:
Скопировать в нее матрицу А и если  количество чисел,
больших К в нечетных столбцах в области 4 больше,
чем произведение чисел в нечетных строках в области 2,
то поменять симметрично области 1 и 3 местами,
иначе 1 и 2 поменять местами несимметрично.
При этом матрица А не меняется.
После чего вычисляется выражение: ((К*A)*F+ K* F T .
Выводятся по мере формирования А, F и
все матричные операции последовательно.
"""


import random

# Функция для чтения матрицы из файла
def read_matrix_from_file(filename,n):
    matrix = []
    with open(filename, 'r') as file:
        for i in range(n):
                row = list(map(int, file.readline().strip().split()))
                matrix.append(row)
    return matrix

# Функция для создания случайной матрицы
def generate_random_matrix(n):
    return [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]

# Функция для подсчета чисел больше K в нечетных столбцах области 4(индексы 1, 3, 5...)
def count_greater_than_k(matrix, k):
    count = 0
    for i in range(len(matrix)):
        if i % 2 == 1:  # Нечетные столбцы
            for j in range(len(matrix)):
                if j > i and j + i > N - 1 and matrix[j][i] > k:  # Область 4
                    count += 1

    print(f"Количество чисел больше {k} в нечётных столбцах области 4: {count}")                    
    return count

# Функция для вычисления произведения элементов в нечетных строках (индексы 1, 3, 5...)
def product_of_odd_rows(matrix):
    product = 1
    found = False
    for i in range(len(matrix)):
        if i % 2 == 1:  # Нечетные строки
            for j in range(len(matrix)):
                if i < j and j + i < N - 1:  # Область 2
                    product *= matrix[i][j]
                    found = True
                    
    print(f"Произведение элементов в нечётных строках области 2: {product}")
    return product if found else 0
    
# Функция для создания матрицы F
def create_f_matrix(A, K):
    N = len(A)
    F = [row[:] for row in A]  # Копируем матрицу A

    count_k = count_greater_than_k(A, K)
    product = product_of_odd_rows(A)

    if count_k > product:
        # Меняем местами области 1 и 3
        print(f"Меняем местами области 1 и 3 симметрично")
        area1_values = []
        area3_values = []

    # Заполняем области 1 и 3
        for i in range(len(F)):
            for j in range(len(F)):
                if i > j and i < N - j - 1:  # Область 1
                    area1_values.append(F[i][j])
                elif i < j and i > N - j - 1:  # Область 3
                    area3_values.append(F[i][j])

    # Исполняем замену значений в областях 1 и 3
        idx_area1 = 0
        idx_area3 = 0

        for i in range(len(F)):
            for j in range(len(F)):
                if i > j and i < N - j - 1:  # Область 1
                    F[i][j] = area3_values[idx_area3]
                    idx_area3 += 1
                elif i < j and i > N - j - 1:  # Область 3
                    F[i][j] = area1_values[idx_area1]
                    idx_area1 += 1

    else:
        # Меняем местами области 1 и 2 несимметрично
        print(f"Меняем местами области 1 и 2 несимметрично")

        for i in range(len(F)):
            for j in range(len(F)):
                  if i > j and i + j < N - 1:
                # Элемент из области 1
                    area1_value = F[i][j]# Соответствующий элемент в области 2
                    area2_value = F[j][i]
                
                # Меняем местами
                    F[i][j] = area2_value
                    F[j][i] = area1_value
    return F

# Функция для вычисления матричного выражения ((K*A)*F + K*F^T)
def matrix_expression(A, F, K):
    N = len(A)
    # Умножение K * A
    KA = [[K * A[i][j] for j in range(N)] for i in range(N)]
    
    # Умножение KA * F
    KAF = [[sum(KA[i][k] * F[k][j] for k in range(N)) for j in range(N)] for i in range(N)]

    # Транспонирование F
    FT = [[F[j][i] for j in range(N)] for i in range(N)]
    
    # Умножение K * F^T
    KF_T = [[K * FT[i][j] for j in range(N)] for i in range(N)]

    # Сложение KAF и KF_T
    result = [[KAF[i][j] + KF_T[i][j] for j in range(N)] for i in range(N)]

    return result

# Основной код
K = int(input("Введите число K: "))

use_file = input("Использовать файл для заполнения матрицы? (да/нет): ").strip().lower()
if use_file == 'да':
    filename = "matrix.txt"
    N = 5
    A = read_matrix_from_file(filename, N)
   
else:
    N = int(input("Введите размерность N матрицы: "))
    A = generate_random_matrix(N)

print("Матрица A:")
for row in A:
    print(row)

F = create_f_matrix(A, K)
print("Матрица F:")
for row in F:
    print(row)

result = matrix_expression(A, F, K)
print("Результат ((K*A)*F + K*F^T):")
for row in result:
    print(row)



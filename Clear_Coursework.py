import matplotlib.pyplot as plt
import pandas as pd

# Гайфуллин Марс КС-28
# Вариант 24

# Исходный массив
massiv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
reshenia = {'Строк': 0, 'Столбцов': 0, 'Метод заполнения': 0, 'Записать в файл': 0,
            'Название файла с исходным массивом': 0, 'Название файла с набором матриц': 0, 'Записать в Excel': 0,
            'Название файла Excel': 0}
# Начало работы
print("Введите количество строк матрицы")
flag = 0
while flag == 0:
    stroka = input()
    if not stroka.isdigit():
        print("Вы ввели не число, попробуйте ещё раз.")
    else:
        flag = 1
        rows = int(stroka)
        reshenia['Строк'] = rows
print("Введите количество чисел в строке матрицы")
flag = 0
while flag == 0:
    stroka = input()
    if not stroka.isdigit():
        print("Вы ввели не число, попробуйте ещё раз.")
    else:
        flag = 1
        numbers = int(stroka)
        reshenia['Столбцов'] = numbers
while flag == 0:
    if rows * numbers > len(massiv):
        flag = 0
        print(
            "Вы ввели некорректные размеры матриц, произведение строк и чисел в строке должно быть не больше количества"
            " элементов! Попробуйте ещё раз. ")
        print("Введите количество строк матрицы")
        rows = int(input())
        reshenia['Строк'] = rows
        print("Введите количество чисел в строке матрицы")
        numbers = int(input())
        reshenia['Столбцов'] = numbers
    else:
        break
print("Как хотите заполнить массивы? По строкам - 1, по столбцам - 2")
way = int(input())

# Количество массивов
number_of_massives = len(massiv) / (numbers * rows)
last_array_check = int(number_of_massives)
if number_of_massives - last_array_check > 0:
    number_of_massives += 1
number_of_massives = int(number_of_massives)
print("Количество массивов:", number_of_massives)

# Создание будущего массива с массивами
massiv_s_massivami = [[[0 for i in range(numbers)] for j in range(rows)] for k in range(number_of_massives)]

# Заполнение массива с массивами
r = 0
if way == 1:
    for i in range(0, int(number_of_massives)):
        for j in range(0, rows):
            for k in range(0, numbers):
                if r >= len(massiv):
                    break
                else:
                    massiv_s_massivami[i][j][k] = massiv[r]
                    r += 1
elif way == 2:
    for i in range(0, int(number_of_massives)):
        for j in range(0, numbers):
            for k in range(0, rows):
                if r >= len(massiv):
                    break
                else:
                    massiv_s_massivami[i][k][j] = massiv[r]
                    r += 1
else:
    print("Некорректно введён способ заполнения")
    exit()
reshenia['Метод заполнения'] = way

print("Ваши матрицы")
for i in range(0, number_of_massives):
    for j in range(0, rows):
        for k in range(0, numbers):
            print(massiv_s_massivami[i][j][k], end=' ')
        print()
    print()

# График зависимости исходного массива от номер элемента в массиве
xlist = massiv
ylist = [i for i in range(0, len(massiv))]
print("Введите название оси Х")
plt.xlabel(input())
print("Введите название оси Y")
plt.ylabel(input())
print("Введите вид маркера: . / o / p / h / +")
marker = str(input())
print("Введите вид линии: - / -- / -. / :")
line = str(input())
print("Введите цвет линии: b / g / r / c")
line_color = str(input())
plt.plot(xlist, ylist, marker + line + line_color)
plt.title("Зависимость элемента массива от его порядкового номера")
plt.show()

# Запись оригинального массива в файл и его считывание
print(
    "Хотите записать исходный массив и полученный набор матриц в файлы и считать их? Введите <<Да>> для продолжения"
    " работы, иначе <<Нет>>.")
decision = input()
if decision == "Да":
    reshenia['Записать в файл'] = decision
    print("Введите название файла для сохранения изначального массива")
    initial_file = input()
    reshenia['Название файла с исходным массивом'] = initial_file + ".txt"
    print("Введите название файла для сохранения набора массивов")
    new_file = input()
    reshenia['Название файла с набором матриц'] = new_file + ".txt"
    file = open(initial_file + ".txt", 'w')
    for i in range(0, len(massiv)):
        file.write(str(massiv[i]) + " ")
    file.close()
    data = []
    with open(initial_file + ".txt", 'r') as f:
        for line in f:
            data.append([int(x) for x in line.split()])
    massiv_schitanniy = data[0]
    print("Массив, прочитанный из файла")
    print(*massiv_schitanniy)

    # Запись набора матриц в файл и его считывание
    data2 = []
    with open(new_file + ".txt", 'w') as h:
        for i in range(0, len(massiv_s_massivami)):
            for j in range(0, rows):
                for k in range(0, numbers):
                    h.write(str(massiv_s_massivami[i][j][k]))
                    h.write(' ')
                h.write('\n')
            h.write('\n')
    massiv_s_massivami_schitanniy = [[[0 for i in range(numbers)] for j in range(rows)] for k in
                                     range(number_of_massives)]

    with open(new_file + ".txt", 'r') as h:
        for line in h:
            if line != "\n":
                data2.append([int(x) for x in line.split()])
    r = 0
    for i in range(0, number_of_massives):
        for j in range(0, rows):
            massiv_s_massivami_schitanniy[i][j] = data2[r]
            r += 1
    print("Набор массивов считанный из файла")
    for array in massiv_s_massivami_schitanniy:
        for line in array:
            for number in line:
                print(number, end=' ')
            print()
        print()
elif decision == "Нет":
    reshenia['Записать в файл'] = decision
    exit()
else:
    print("Ваш ответ непонятен")

# Запись исходного массива и набора матриц в файлы Excel
print(
    "Хотите вывести исходный массив и полученные матрицы в таблицу Excel? Введите <<Да>> для продолжения работы, иначе"
    " <<Нет>>.")
decision = input()
if decision == "Да":
    reshenia['Записать в Excel'] = decision
    print("Введите название файла")
    name_of_file = input()
    reshenia['Название файла Excel'] = name_of_file + ".xlsx"
    df1 = pd.DataFrame({
        'Initial array': massiv
    })
    df2 = pd.DataFrame({
        'New array': massiv_s_massivami
    })
    with pd.ExcelWriter(name_of_file + ".xlsx") as writer:
        df1.to_excel(writer, 'Old')
        df2.to_excel(writer, 'New')

elif decision == "Нет":
    reshenia['Записать в Excel'] = decision
    exit()
else:
    print("Ваш ответ непонятен")

# Запись в бинарный файл
print("Бинарный файл с вашими решениями: desicions.bin")
b = open("decisions.bin", 'wb')
for key in reshenia.keys():
    skey = key + "\n"
    svalue = str(reshenia[key]) + "\n"
    b_key = skey.encode()
    b_value = svalue.encode()
    b.write(b_key)
    b.write(b_value)
b.close()

# Чтение бинарного файла
b = open('decisions.bin', 'rb')

D2 = dict()

b_strings = b.readlines()  # b_strings - список строк типа bytes

#     Сначала читается ключ, затем значение и т.д.
fkey = True
for item in b_strings:
    if fkey:
        skey = item.decode()
        key = skey[:-1]
        fkey = False
    else:
        svalue = item.decode()
        D2[key] = svalue[:-1]
        fkey = True

print("Ваши решения в проделанной работе программы:")
print("D2 = ", D2)

b.close()

# Написати fizzbuzz для 20 комплектів по три числа, які записані в файл.
# Читайте із файлу перший рядок з трьома числами, беріть із нього числа,
# рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком і так до кінця файла.
f = open('Home_3_2_set_numbers.txt', 'r') # в файлі тепер file descriptor
for line in f: # для кожного рядка у файлі
    my_split = line.rstrip().split(',')
    a = int(my_split[0])
    b = int(my_split[1])
    c = int(my_split[2])
    print('a=', a, 'b=', b, 'c=', c)
    answ = ''
    for el in range(1, c + 1):
        if el % (a * b) == 0:
            answ += 'FB '
        elif el % a == 0:
            answ += 'F '
        elif el % b == 0:
            answ += 'B '
        else:
            answ += str(el) + ' '
    print(answ)
f.close() # закриття файлу







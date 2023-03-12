# Написати fizzbuzz для 20 комплектів по три числа, які записані в файл.
# Читайте із файлу перший рядок з трьома числами, беріть із нього числа,
# рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком і так до кінця файла.
f = open('Home_3_2_set_numbers.txt', 'r') # в файлі тепер file descriptor
for line in f: # для кожного рядка у файлі
    my_split = line.rstrip().split(',')
    a, b, c, = int(my_split[0]), int(my_split[1]), int(my_split[2])
    print('a=', a, 'b=', b, 'c=', c)
    answ = str(['FB' if not el % (a * b) else 'F' if not el % a else 'B' if not el % b else el
                for el in range(1, int(c) + 1)]).replace('\'', '')[1:-1]
    print(answ)
f.close() # закриття файлу







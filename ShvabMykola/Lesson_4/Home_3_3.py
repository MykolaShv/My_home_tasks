# Переробити другу задачу так, щоб результат писався в інший файл.
f = open('Home_3_2_set_numbers.txt', 'r')
f1 = open('Home_3_3_result.txt', 'wt')
for line in f: # для кожного рядка у файлі
    my_split = line.rstrip().split(',')
    a, b, c, = int(my_split[0]), int(my_split[1]), int(my_split[2])
    answ = 'set: ' + line + str(['FB' if not el % (a * b) else 'F' if not el % a else 'B' if not el % b
                                else el for el in range(1, int(c) + 1)]).replace('\'', '')[1:-1]
    f1.write(answ + '\n')
f.close()
f1.close()







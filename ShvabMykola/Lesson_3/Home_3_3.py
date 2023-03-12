# Переробити другу задачу так, щоб результат писався в інший файл.
f = open('Home_3_2_set_numbers.txt', 'r')
f1 = open('Home_3_3_result.txt', 'wt')
for line in f: # для кожного рядка у файлі
    my_split = line.rstrip().split(',')
    a = int(my_split[0])
    b = int(my_split[1])
    c = int(my_split[2])
    answ = 'set: ' + line
    for el in range(1, c + 1):
        if el % (a * b) == 0:
            answ += 'FB '
        elif el % a == 0:
            answ += 'F '
        elif el % b == 0:
            answ += 'B '
        else:
            answ += str(el) + ' '
    f1.write(answ + '\n')
f.close()
f1.close()







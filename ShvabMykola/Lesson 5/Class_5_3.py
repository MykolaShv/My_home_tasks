# Візьміть файл, в якому є багато англійських слів у рядках.
# Порахуйте частоту зустрічі кожного слова та видрукуйте відсортовано.
def read_file(name):
    with open(name, 'r') as f:
        return f.read()
name = 'My_text.txt'
t = read_file(name).lower()
for i in ['.', ',', '!', ':', ';', '?', '-', '(', ')', '\"']:
    t = t.replace(i, '1')
t = t.split()
# рахуємо кожне слово
my_dic = {}
for word in t:
    k = t.count(word)
    my_dic[word] = k
#  сортуємо числа повторень, тому key=lambda item: item[1]
my_dic = sorted(my_dic.items(), key=lambda item: item[1], reverse=True)
# виводимо на екран
for el in my_dic:
    it, val = str(el).split(',')
    it = it[2:-1]
    val = val[:-1]
    print(f'the word {it} is reapeted {val} times' if int(val) > 1 else f'the word {it} is reapeted 1 time')

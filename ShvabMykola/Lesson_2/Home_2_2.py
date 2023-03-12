# Другий рівень ("if-elif-else"):
# Придумати власні приклади на альтернативні варіанти if і активне використання булевої алгебри.
# Дано якийсь список, наприклад [1, 3, 5, 7, 9, 11, 13, 15]

l = input('Input list, any number from 1 till 15, min length of the list = 5   ')
a = input('Input any number from 1 till 15, a  ')
b = input('Input any number from 1 till 15, b  ')
c = input('Input any number from 1 till 15, c  ')
'''
допоміжне, для написання програми та тестування
l = [1, 3, 5, 7, 9, 11, 13, 15]
a, b, c = 2, 5, 7
'''
#  Чи входить в ньому число a або b?
print(l, ' a = ', a, ' b = ', b, ' c = ', c)
print('Чи входить в ньому число a або b? True' if a in l or b in l else 'Чи входить в ньому число a або b? False')
#  Чи входить в ньому число a та b?
print('Чи входить в ньому число a та b? True' if a in l and b in l else 'Чи входить в ньому число a та b? False')
#  Чи входить в ньому a та b або c?
print('Чи входить в ньому a та b або c? True' if a in l and b in l or c in l else 'Чи входить в ньому a та b або c? False')
#  Чи входить в ньому a або b та c?
print('Чи входить в ньому a або b та c? True' if a in l and b in l or c in l else 'Чи входить в ньому a або b та c? False')
#  Чи входить в ньому a та b та c?
print('Чи входить в ньому a та b та c? True' if a in l and b in l and c in l else 'Чи входить в ньому a та b та c? False')
#  Чи входить в ньому a або b або c?
print('Чи входить в ньому a та b та c? True' if a in l or b in l or c in l else 'Чи входить в ньому a та b та c? False')



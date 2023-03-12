# Перший рівень ("if"): Набрати всі приклади посимвольно і змусити їх працювати, розібратися у роботі.
print ("Give it to me!")
number = int(input())

if (number >= 100):
    print ("Thanks, man!")
elif ((number > 10) and (number < 100)):
    print ("OK :(")
else:
    print ("WHAAAAT????")

if (number > 1000):
    print ("!!!!WOOOOWWWW!!!")

x = 5
y = 10
z = 15
print('(x < y) and (y <= z): ',(x < y) and (y <= z))
print('x < y <= z: ',x < y <= z)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print('l1 == l2 :',l1 == l2)
print('l1 is l2 :',l1 is l2)
print('l1 is not l2 :',l1 is not l2)

l1 = [1, 2, 3]
print('3 in l1: ',3 in l1)
print('4 in l1: ',4 in l1)
print('5 not in l1: ',5 not in l1)

test = True
result = 'Test is True' if test else 'Test is False'
print(result)

test = True
print('ttt' if test else 'fff')

test = True
result = test and 'Test is True' or 'Test is False'
print(result)



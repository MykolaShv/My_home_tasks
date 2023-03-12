# Ввести число, вивести його розряди та їх множники.
my_number = int(input('please, input your number '))
print('You have inputed :', my_number)
str_number = str(my_number)
n = len(str_number)
answ = ''
for id, item in enumerate(str_number):
    answ += str(item) +  '*' + str(10**(n-id-1)) + ' + '
print('The answer is: ', answ[:-2])

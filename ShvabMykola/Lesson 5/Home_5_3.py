# написати пари - номера чисел та їх парність використовуючи zip
n = int(input('Введіть число: '))
list_numbers = []
list_odds = []
for i in range(1,n+1):
    list_numbers.append(str(i))
    if i % 2:
        list_odds.append('непарне')
    else:
        list_odds.append('парне')
print(dict(zip(list_numbers, list_odds)))
# вивести  списки із обєднаними 3 списками, перевіривши чи вони мають одну ж довжину

list1 = 'abcdefj'
list2 = [55,43,38,117,2]
list3 = ['blue', 'yellow', 'green', 'red', 'black']
def short(*args):
    return range(len(sorted(args, key = len)[0]))
answ = ((list1[i], list2[i], list3[i]) for i in short(list1,list2,list3))
for item in answ:
    print(item)
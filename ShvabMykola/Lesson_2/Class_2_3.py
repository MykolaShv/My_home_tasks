from math import sqrt
my_number = int(input('please, input your number '))
print('You have inputed :', my_number)
list_answers = []
# щоб зменшити кількість ітерацій, треба добути квадратний корінь
max_div = int(sqrt(my_number))
for i in range(1, max_div+1):
    # до початкового списку добавляємо дільник(якщо ділиться на ціло), також потрібно знайти обернений дільни
    #  адже ми добули корінь і ті дільники загубляться, якщо не ціле число - добавляємо 0
    list_answers.append(i) or list_answers.append(int(my_number/i)) if my_number%i == 0 else list_answers.append(0)
# сортуємо для красоти
list_answers.sort()
# треба вирішити питання по повторенню елементів. 0 буде багато. Також якщо 36/6 - буде дві цифри 6,
# їх треба  видалити, створюємо новий список
answer_list = []
for element in list_answers:
    if element not in answer_list:
        answer_list.append(element)
# за умовою 1 і саме введене число треба убрати із списку
del answer_list[:2]
del answer_list[-1]
# убираємо дужки, а також передбачаємо якщо буде введено ПРОСТЕ число, тобто останній список буде пустим
print('Its dividers are :' + str(answer_list)[1:-1] if answer_list else 'No deviders')

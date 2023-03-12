# Банкомат видає суму максимально можливими купюрами
# створюємо список банкнотів, хочеться задати не тривіальний
banknotes = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
# сортуємо в порядку зпадання
sorted_banknotes = sorted(banknotes, reverse=True)
# просимо ввести число
my_summ = int(input('Please the necessary amount to take: '))
my_summ1 = my_summ
# задаємо список кількості банкнотів та створюємо
quantity_banknotes = []
for el in sorted_banknotes:
	qb = my_summ1 // el
	quantity_banknotes.append(qb)
	my_summ1 -= qb*el
len_banknotes = len(sorted_banknotes)
print('To take necessary amount: ', my_summ, ' you need the following banknotes in such quantity: ')
for i in range(len_banknotes):
	if quantity_banknotes[i]:
		print('nominal banknote', sorted_banknotes[i], ' - number: ', quantity_banknotes[i])





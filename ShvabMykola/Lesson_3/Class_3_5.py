# Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри
# створюємо список банкнотів
banknotes = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
# просимо ввести число
my_summ = int(input('Please the necessary amount to take: '))
# задаємо список кількості банкнотів та створюємо
quantity_banknotes = []
len_banknotes = len(banknotes)
amm = 0
new_bank = []
# частина 1 - надаємо всім номіналам по 10 банкнотів до тих пір коли не появиться відємне число
for i in range(len_banknotes):
	q = 10*banknotes[i]
	new_bank.append(banknotes[i])
	amm += q
	if amm < my_summ:
		quantity_banknotes.append(i)
	else:
		quantity_banknotes.append(i)
		break
my_summ1 = my_summ - amm
# частина 2 - розкладаємо різницю по максимуму
sorted_banknotes = sorted(new_bank, reverse=True)
len_sor = len(sorted_banknotes)
quantity_banknotes1 = []
for el in sorted_banknotes:
	qb = -my_summ1 // el
	quantity_banknotes1.append(qb)
	my_summ1 += qb*el
# частина 3 - виводимо на екран, але коригуємо кількість банкнотів на кількість зайвих -
# вони визначенні в частині 2
for i in range(len_sor):
	print('nominal banknote', sorted_banknotes[i], ' - number: ', 10-quantity_banknotes1[i])


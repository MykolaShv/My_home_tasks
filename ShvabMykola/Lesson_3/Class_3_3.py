# Написати програму, яка виводить сама себе задом наперед
import sys
filename = sys.argv[0]
# далі відкриваємо файл для читання (опція 'r')
f = open(filename, 'r') # в файлі тепер file descriptor
for line in f: # для кожного рядка у файлі
	print(line[::-1], end='')
f.close() # закриття файлу





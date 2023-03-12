# Перевірити, чи є число не парним, ділиться чи на три і на п'ять одночасно, але так, щоб не ділитися на 10.

my_number = int(input('please, input your number '))
print('That is' if my_number%2 and my_number%10 and  my_number%3 == 0 and  my_number%5 == 0 else 'Not that')

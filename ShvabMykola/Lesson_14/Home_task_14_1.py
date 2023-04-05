class Phone:
    phone_number = ''
    _count_calls = 0

    def change_number(self, phone_number):
        print(phone_number, ' has changed')
        return phone_number

    def output_count_callings(self):
        return self._count_calls

    def count_callings(self):
        self._count_calls += 1

my_phone = Phone()
my_phone.change_number('111-11-11')
his_phone = Phone()
his_phone.change_number('222-22-22')
her_phone = Phone()
her_phone.change_number('333-33-33')

my_phone.count_callings()
my_phone.count_callings()
my_phone.count_callings()
my_phone.count_callings()
my_phone.count_callings()
my_phone.count_callings()
my_phone.count_callings()
his_phone.count_callings()
his_phone.count_callings()
her_phone.count_callings()
her_phone.count_callings()
her_phone.count_callings()
print(my_phone.output_count_callings())
print(his_phone.output_count_callings())
print(her_phone.output_count_callings())

list_phones = (my_phone, his_phone, her_phone)

def number_calls(list_phones):
    print(f'The total amount of calls are {sum([_.output_count_callings() for _ in list_phones])}')

number_calls(list_phones)

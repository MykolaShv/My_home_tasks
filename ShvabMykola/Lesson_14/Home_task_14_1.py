class Phone:
    phone_number = '555-55-55'
    _count_calls = 0

    def change_number(self):
        return phone_number

    def output_count_callings(self):
        return self._count_calls

    def count_callings(self):
        self._count_calls += 1
        return self._count_calls


class My_phone(Phone):
    _count_calls = 0


class His_phone(Phone):
    _count_calls = 0


class Her_phone(Phone):
    _count_calls = 0


my_phone = My_phone()
phone_number = '111-11-11'
my_ph = my_phone.change_number()
my_phone.count_callings()
my_phone.count_callings()
my_phone.count_callings()
my_phone.count_callings()
my_phone.count_callings()
my_phone.count_callings()
my_phone.count_callings()
my_out_ph = my_phone.output_count_callings()


his_phone = His_phone()
phone_number = '222-22-22'
his_ph = his_phone.change_number()
his_phone.count_callings()
his_phone.count_callings()
his_out_ph =  his_phone.output_count_callings()

her_phone = Her_phone()
phone_number = '333-33-33'
her_ph = her_phone.change_number()
her_phone.count_callings()
her_phone.count_callings()
her_phone.count_callings()
her_out_ph = her_phone.output_count_callings()

def number_calls():
    list_phone = (my_ph, his_ph, her_ph)
    list_out_ph = (my_out_ph, his_out_ph, her_out_ph)
    all_calls = sum(list_out_ph)
    answer = zip(list_phone, list_out_ph)
    print([f'this number {key} has recieved {value} calls ' for key, value in answer])
    print('Total amount of calls is ', all_calls, ' calls.')

number_calls()
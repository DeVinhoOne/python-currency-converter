import requests

from show_additional_info import show_additional_info

print('\n\t\t===Currency Converter===')
show_info = input('\tDo You need additional info?(y/n) ').lower()

if show_info == 'y':
    show_additional_info()
elif show_info == 'n':
    pass


class Converter:
    def __init__(self):
        self.amount = float(
            input('\n\tHow much money do You want to convert? '))
        self.base_currency = input('\tWhat is Your base currency? ').upper()
        self.rates = None

        self.convert()
        self.printer()

    def convert(self):
        req = requests.get('https://api.exchangeratesapi.io/latest',
                           params={'base': self.base_currency})
        self.rates = req.json()['rates']

    def printer(self):
        print(f'\n{self.amount}{self.base_currency} converted into..\n')
        for currency, rate in self.rates.items():
            converted_amount = round(rate * self.amount, 2)

            print(f'{currency} => {converted_amount}')


cc = Converter()

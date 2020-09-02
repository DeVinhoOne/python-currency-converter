import requests

print('\n===Currency Converter===\n')
amount = float(input('\tHow much money do You want to convert? '))
from_currency = input('\tWhat is Your base currency? ').upper()
to_currency = input('\tWhat currency do You want to get? ').upper()

req = requests.get('https://api.exchangeratesapi.io/latest',
                   params={'base': from_currency})
target_rate = req.json()['rates'][to_currency]


value = amount * target_rate
print(f'\n{amount}{from_currency} ===> {round(value, 2)}{to_currency}\n')

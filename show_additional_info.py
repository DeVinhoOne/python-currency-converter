import requests


def show_additional_info():
    print('\nWelcome in Currency Converter. This simple console program allows you to convert money into most popular currencies from all over the world. Please use 3 letter shortcut when You are asked to enter currency (e.g. USD for US Dollar).')
    show_currencies = input(
        '\nDo You want to check all supported currencies?(y/n) ').lower()

    if show_currencies == 'y':
        req = requests.get('https://api.exchangeratesapi.io/latest')
        rates = req.json()['rates']

        for rate in rates:
            print(rate)

    elif show_currencies == 'n':
        pass

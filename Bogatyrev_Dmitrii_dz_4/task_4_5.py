import utils

if __name__ == '__main__':
    import sys

    if type(sys.argv) == list and len(sys.argv) > 1:
        program, currency_name = sys.argv
        kurs, date_value = utils.currency_rates_adv(currency_name)
        print(kurs, date_value)
    else:
        currencies_list = ["usd", "USD", "eur", "EUR", "noname"]

        for i in currencies_list:
            kurs, date_value = utils.currency_rates_adv(i)
            utils.check_values(kurs, date_value)
            print(kurs, date_value)

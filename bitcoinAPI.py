import requests

def main():
    users_number_of_bitcoin = float(input('How many bitcoin do you have?: '))
    bitcoin_to_dollars_rate = api()
    USD = convert(users_number_of_bitcoin, bitcoin_to_dollars_rate)
    display(USD)


def api():
    bitcoin_current_price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    rate = bitcoin_current_price['bpi']['USD']['rate_float']
    return rate


def convert(number_of_bitcoin, rate):
    USD = rate * number_of_bitcoin
    return USD


def display(USD):
    print('Your bitcoin is worth ${:.2f}'.format(USD))


if __name__ == '__main__':
    main()
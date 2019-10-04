import requests

bitcoin_current_price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
rate = bitcoin_current_price['bpi']['USD']['rate_float']
users_number_of_bitcoin = float(input('How many bitcoin do you have?: '))
USD = rate * users_number_of_bitcoin
print(USD)
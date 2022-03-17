import app.requests as requests



def convert_currency(from_c,to_c):
   API_KEY = '7R56N1UXR8X8CBH5'

   url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(
			from_c, to_c, API_KEY)
   response = requests.get(url=url).json()

   return response

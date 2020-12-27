import yfinance as yf


def get_data(ticker):
	
	data_day = yf.Ticker(ticker).history(
		period='2d', interval='1d'
	)
	data_5_min = yf.Ticker(ticker).history(
		period='10m', interval='5m'
	)
	
	return data_day, data_5_min


if __name__ == '__main__':
	print(get_data('SBER.ME'))
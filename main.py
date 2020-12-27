import pickle
import yfinance as yf
from utils.send_message import send_message
from utils.check_time_condition import check_time_condition
from utils.get_data import get_data

with open('data/dict_of_open_minus_low_abs_day.pickle', 'rb') as file:
	DICT_OF_OPEN_MINUS_LOW_ABS_DAY = pickle.load(file)
with open('data/dict_of_mean_ranges_per_5_min.pickle', 'rb') as file:
	DICT_OF_MEAN_RANGES_PER_5_MIN = pickle.load(file)
RUS_STOCKS = [
	ticker for ticker in DICT_OF_OPEN_MINUS_LOW_ABS_DAY if '.ME' in ticker
]

while True:
	
	for ticker in DICT_OF_OPEN_MINUS_LOW_ABS_DAY:		
		
		# Checks whether the russian stock market is open
		time_condition = check_time_condition()
		if ticker in RUS_STOCKS and time_condition:
			continue
		
		data_day, data_5_min = get_data(ticker)
		
		range_day = (
			abs(data_day.Open[-1] - data_day.Close[-1]) / data_day.Open[-1]
		)
		range_5min = (
			(data_5_min.High[-2:] - data_5_min.Low[-2:]) / data_5_min.Low[-2:]
		)
		
		cond_day = range_day > DICT_OF_OPEN_MINUS_LOW_ABS_DAY[ticker]
		cond_5min = all(range_5min < DICT_OF_MEAN_RANGES_PER_5_MIN[ticker])
		if cond_day and cond_5min:
			send_message(ticker)
			print(ticker)
		
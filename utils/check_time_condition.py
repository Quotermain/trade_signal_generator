import datetime


def check_time_condition():
	
	time_condition = (
		datetime.datetime.now().weekday() in [5, 6] or
		(
			datetime.datetime.now().time() < datetime.time(12, 0, 0) and
			datetime.datetime.now().time() > datetime.time(20, 45, 0)
		)
	)
	
	return time_condition


if __name__ == '__main__':
	print(check_time_condition())
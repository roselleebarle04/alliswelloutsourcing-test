import datetime
import re

def format_datetime_string(input):
	output = re.findall(r"(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})", input)[0]
	return datetime.datetime(int(output[0]), int(output[1]), int(output[2]), int(output[3]), int(output[4]), int(output[5]))

def format_output_string(input):
	seconds_in_minute = 60
	seconds_in_hour = 60 * seconds_in_minute
	seconds_in_day = 24 * seconds_in_hour

	total_seconds = input.total_seconds()
	total_days = total_seconds / seconds_in_day
	total_minutes = total_seconds / seconds_in_minute
	total_hours = total_seconds / seconds_in_hour
	return "%s Days %s Hours %s Minutes %s Seconds" % (total_days, total_hours, total_minutes, total_seconds)


def solution():
	"""
	Computes the time difference between two datetime strings, and outputs the result into equivalent 
	days, hours, minutes and seconds. 
	"""
	startDateTime = str(20160104173643)
	endDateTime = str(20160521101256)
	timeDifference = format_datetime_string(endDateTime) - format_datetime_string(startDateTime)

	print(format_output_string(timeDifference))
	return format_output_string(timeDifference)


solution()

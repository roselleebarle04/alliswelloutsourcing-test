import datetime
import re


def format_datetime_string(input):
    output = re.findall(r"(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})", input)[0]
    return datetime.datetime(int(output[0]), int(output[1]), int(output[2]), int(output[3]), int(output[4]),
                             int(output[5]))


def format_output_string(input):
    seconds_in_minute = 60
    seconds_in_hour = 60 * seconds_in_minute
    seconds_in_day = 24 * seconds_in_hour

    total_seconds = input.total_seconds()
    days = divmod(total_seconds, 86400)  # days
    hours = divmod(days[1], 3600)  # hours
    minutes = divmod(hours[1], 60)  # minutes
    seconds = minutes[1]  # seconds
    return "%s Days %s Hours %s Minutes %s Seconds" % (days[0], hours[0], minutes[0], seconds)


def solution():
    """
    Computes the time difference between two datetime strings, and outputs the result into equivalent
    days, hours, minutes and seconds.
    """
    startDateTime = str(20160104173643)
    endDateTime = str(20160521101256)
    timeDifference = format_datetime_string(endDateTime) - format_datetime_string(startDateTime)
    print format_output_string(timeDifference)
    return format_output_string(timeDifference)


solution()

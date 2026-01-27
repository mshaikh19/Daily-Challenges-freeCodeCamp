# Odd or Even Day
# Given a timestamp (number of milliseconds since the Unix epoch), return:

# "odd" if the day of the month for that timestamp is odd.
# "even" if the day of the month for that timestamp is even.
# For example, given 1769472000000, a timestamp for January 27th, 2026, return "odd" because the day number (27) is an odd number.

import datetime

def odd_or_even_day(timestamp):
    
    # Get seconds from milliseconds
    seconds = timestamp / 1000.0

    # Extract date and time from the timestamp seconds
    dateAndTime = datetime.datetime.fromtimestamp(seconds, datetime.timezone.utc)

    # Extract day from the date and time
    day = dateAndTime.day
    
    # Find if the day extracted is even
    if day % 2 == 0:
        return "even"

    return "odd"

print(odd_or_even_day(1769472000000))
print(odd_or_even_day(1769444440000))
print(odd_or_even_day(6739456780000))
print(odd_or_even_day(1))
print(odd_or_even_day(86400000))
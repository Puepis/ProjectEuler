
'''Description: PEuler 19 - Counting Sundays

   Q: How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

   Explanation: Brute force - solution can be used for any range of years (within reason)

   Date: August 25, 2019
'''

def main():

    years = range(1901, 2001)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    num_days = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, \
        "October": 31, "November": 30, "December": 31}
    day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # January 1, 1900 was a Monday - find Jan 1, 1901 day
    if is_leap_year(1900):
        num_days["February"] = 29

    # Starting day
    day = (1 + sum(num_days.values())) % 7
    print("Number of days in 1900: " + str(sum(num_days.values())))
    print("Jan 1, 1901: " + day_list[day])

    days_on_first = []
    for year in years:

        # Leap year
        if is_leap_year(year):
            num_days["February"] = 29
        else:
            num_days["February"] = 28

        # Day of first of the month
        for month in months:
            day += num_days[month]
            day = day % 7
            days_on_first.append(day_list[day])

    # Number of sundays on the first of the month in the 20th century
    print("Number of Sundays: " + str(days_on_first.count("Sunday")))

def is_leap_year(year):

    # Not multiple of 4
    if year % 4 != 0:
        return False

    # Multiple of 4, not a century
    elif year % 100 != 0:
        return True

    # Century divisible by 400
    elif year % 400 == 0:
        return True

    # Century not divisible by 400
    else:
        return False

main()

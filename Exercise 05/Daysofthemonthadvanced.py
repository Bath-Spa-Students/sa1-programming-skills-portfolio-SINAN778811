#Creating a dictionary, assosciating each month with its total number of days.
Number_of_days = {
    # January
    1:31,
    # February
    2:28,
    # March
    3:31,
    # April
    4:30,
    # May
    5:31,
    # June
    6:30,
    # July
    7:31,
    # August 
    8:31,
    # September
    9:30,
    # October
    10:31,
    # November
    11:30,
    # December
    12:31,

}

# inquiring the user to enter the month number. 
month_number = int(input("Type your month number:")) 
calender_year = int(input("Type the year:"))

# Requesting the user if the year is a leap year and modifying February's day count.
if month_number in Number_of_days:
    if month_number == 2:
        leap_year = input(f"{calender_year} is a leap year?")
        if leap_year == "yes":
            print(f"The no.of days in month {month_number} of year {calender_year} is 29 a leap year.")
        else:
            print(f"The no.of days in month {month_number} of year {calender_year} is 28.")
    else:
        print(f"The number of days in month {month_number} is {calender_year[month_number]}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
  
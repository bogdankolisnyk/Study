seconds_input = int(input("Enter number of seconds (0 to 8639999): "))

if 0 <= seconds_input < 8640000:

    days, remainder = divmod(seconds_input, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days == 1:
        day_word = "day"
    else:
        day_word = "days"
    formatted_time = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    print(formatted_time)
else:
    print("Invalid input! Number of seconds must be between 0 and 8639999.")
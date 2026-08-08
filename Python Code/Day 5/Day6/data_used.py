def daily_data(user_name,used_data,data_limit):
    remaing = data_limit - used_data

    print("User = ",user_name)
    print("Data use = ",used_data)
    print("Data Left = ",remaing)

    if remaing <= 0:
        message = "You have used your 100% data"

    elif remaing <= 0.5:
        message = "Warning you have only 50% of your data"

    else:
        message = "You have data to used "

    print("SMS message send", message)

daily_data("prerna",1.5,5.0)
daily_data("Rosh",2.0,5.0)
daily_data("Sakshi",1.5,2.0)

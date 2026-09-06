def calculate_bill(movie , seat):

    tickit_amount = movie["price"] * seat

    gst = tickit_amount * 18/100

    final_amount = tickit_amount + gst

    print("\n===movie Bill===")

    print("Movie :",movie["name"])
    print("Genre :",movie["genre"])
    print("Ticket Price :",movie["price"])
    print("Seats  :",movie)

    print("---------------------")

    print("Ticket Amount :", tickit_amount)
    print("GST (18%)     :", gst)
    print("Grand Total   :" , final_amount)

    print("======================")
    return final_amount
movie = []

try:
    movie_name = (input("Enter the movie name :"))
    age = int(input("Enter the age : "))
    ticket = int(input("Enter number of ticket :"))
    price = int(input("Enter the price :"))

   

    item = {
        "movie" : movie_name,
        "age"   : age,
        "Ticket" : ticket,
        "Price" : price
    }

    movie.append(item)

    for item in movie:
        total = item["Price"] * item["Ticket"]
        print("Total Price",total)
except ValueError as e:
    print("Error :",e)
finally:
    print("Thankyou for Booking Movie  ")
    
    

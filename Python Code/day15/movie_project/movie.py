movies = []

def add_movie(movie_id,name,genre,price):
    movie = {
        "id" : movie_id,
        "name" : name,
        "genre" : genre,
        "price" : price
    }

    movies.append(movie)

    print("Movies added successfully")

    def display_movie():

        if not movies:
            print("No movies available.")
            return

        print("\n----------MOVIES------------")

        for movie in movies:

            print(
                movie["id"],
                "|",
                movie["name"],
                "|",
                movie["genre"],
                "|",
                movie["price"],
                "|"
            )

    def search_movie(name):

        for movie in movies:

            if movie["name"].lower() == name.lower():

                print("\nMovies Found")
                print("ID:",movies["id"])
                print("Name :",movie["name"])
                print("Genre :", movie["genre"])
                print("Ticket Price :", movie["price"])

                return movie

        print ("Movie not Found.")
        return None
movies = {
    "Avengers": {"price": 1500, "seats": 30},
    "Oppenheimer": {"price": 2000, "seats": 20},
    "Barbie": {"price": 1200, "seats": 50}
}



def view_movies():
    print("----Available Movies----")
    for key, value in movies.items():
        price = value["price"]
        seats = value["seats"]

        print(f"{key}: ${price} ({seats} seats left)")

def book_ticket():
    movie_name = input("Enter the name of the movie you'll like to watch? ").capitalize().strip()
    if movie_name not in movies:
        print(f"{movie_name} not found")
        return
    try:
        num_tickets = int(input(f"How many tickets for {movie_name} would you like ? ").strip())
        if num_tickets <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    available_seats = movies[movie_name]["seats"]
    ticket_price = movies[movie_name]["price"]

    if num_tickets > available_seats:
        print("Not enough seats available")
        return
    else:
        total = num_tickets * ticket_price
        movies[movie_name]["seats"] -= num_tickets
        print(f"Booking for {movie_name} successful! You paid ${total}")
        print(f"{movies[movie_name]["seats"]} seats remaining")

def main():
    while True:
        print()
        print("=== Movie Ticket Booking System ===")
        print("1. View Movies")
        print("2. Book Ticket")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()
        print()

        if choice == "1":
            view_movies()

        elif choice == "2":
            book_ticket()

        elif choice == "3":
            print("Are you sure you want to exit Y/N")
            ans = input("Enter Y to stay or N to exit ").upper().strip()
            if ans == "N":
                main()
            elif ans == "Y":
                print("Goodbye! Thanks for using our ticket booking system.")
                break
            else:
                print("Invalid input. Please enter Y or N ")               

        else:
            print("Invalid option. Please try again.")            


main()

#view_movies()
#book_ticket()

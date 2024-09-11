MENU_PROMPT = "\nEnter 'a' to add movie 'l' to list the movies 'f' find the movie name 'd' for delete the movie 'q' to quit. "

movies = []

def add_movies():
    title = input("Enter the movie name:")
    director = input("enter the director name:")
    year = input("enter the year:")

    movies.append({
        'title':title,
        'director' : director,
        'year' : year
    })
    print(movies)

def show_movies():
    for movie in movies:
        print_movie(movie)



def find_movies():
    search_title = input("enter title to search:")
    for movie in movies:
        if search_title == movie['title']:
            print_movie(movie)

def delete_movies():
    delete_search = input("enter the title:")
    for movie in movies:
        if delete_search != movie[("title")]:
            print_movie(movie)



def menu():
    selection = input(MENU_PROMPT).lower()
    while selection != 'q':
        if selection == 'a':
            add_movies()
        elif selection == 'l':
            show_movies()
        elif selection == 'f':
            find_movies()
        elif selection == 'd':
            delete_movies()
        else:
            print("Please try again correct command")
        selection = input(MENU_PROMPT).lower()
menu()
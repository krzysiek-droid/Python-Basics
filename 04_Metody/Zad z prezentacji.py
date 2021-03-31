def get_books_w_marks():
    counter = int(input("Give the number books you want to add: "))
    books_collection = []
    for book in range(counter):
        book_title = input("Insert book name here: ").capitalize()
        rate = int(input("Give it a rate in range of 1 to 10: "))
        books_collection.append([book_title,rate])
    return books_collection

def show_rate(books_collection):
    book_number = int(input("Insert a book number you want to see: "))
    indx = book_number - 1
    print(f"You have choosen book {books_collection[indx][0]} that has a rate of {books_collection[indx][1]}")

def search_database(books_collection):
    user_numb = int(input("Give the number you want to check: "))
    for i in range(len(books_collection)):
        if user_numb == books_collection[i]:
            print(f"Your number is in database, with #{i}")
        else:
            print(f"There is no such number in given database")
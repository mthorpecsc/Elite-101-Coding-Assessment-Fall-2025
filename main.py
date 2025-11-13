#from library_books import library_books
from datetime import datetime, timedelta
import time 
library_books = [
    {
        "id": "B1",
        "title": "The Lightning Thief",
        "author": "Rick Riordan",
        "genre": "Fantasy",
        "available": True,
        "due_date": None,
        "checkouts": 2
    },
    {
        "id": "B2",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Historical",
        "available": False,
        "due_date": "2025-11-01",
        "checkouts": 5
    },
    {
        "id": "B3",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "available": True,
        "due_date": None,
        "checkouts": 3
    },
    {
        "id": "B4",
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "available": True,
        "due_date": None,
        "checkouts": 4
    },
    {
        "id": "B5",
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "available": True,
        "due_date": None,
        "checkouts": 6
    },
    {
        "id": "B6",
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "available": False,
        "due_date": "2025-11-10",
        "checkouts": 8
    },
    {
        "id": "B7",
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "genre": "Science Fiction",
        "available": True,
        "due_date": None,
        "checkouts": 1
    },
    {
        "id": "B8",
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-Age",
        "available": False,
        "due_date": "2025-11-12",
        "checkouts": 3
    }
]

#lvl 1 psuedo code 
'''
create a function title viewbooks
make a class called book?
if the book is unavailble, create an if statement to not print out
create a for loop that prints out the books and proper information

'''
#creating a book class to let new books be created in the future 
class Books:
    def __init__(self, id, title, author, genre, available, due_date, checkouts):
     self.id = id
     self.title = title
     self.author = author
     self.genre = genre
     self.available = available 
     self.due_date = due_date
     self.checkouts = checkouts


#function that allows us to view the available books
def view_books():
   print("Welcome to the Local Library! \nHere you can view all of the available books. \nLook down below for our current collection!")
   print()
   time.sleep(3)
   for book in library_books:
    #iterating through each book in the dictionary
    if book["available"] == True:
      #if the book is availble it'll print out the id, title, and author
      print(f'Book ID: {book["id"]}, \nBook Title: {book["title"]}, \nAuthor: {book["author"]}')
      print('-'*15)


#lvl 2 pseudo code
"""
create a function called book_search
allow users to input an authors name 
if statements to determine whether the author is found in the dictionary or not
give a print statments giving matching/found results
allows users to input a genre
use if statements to see if the genre is available
return print statement of whether matches were found or not

"""

def main_menu():
    print("Placeholder for main menu!")



def book_search():
    print("Welcome to the Book Search!")
    choice = input("Would you like to search by author or genre? ")
    if choice.lower() == 'author':
        print('-'*30)
        find_author()
    elif choice.lower() == 'genre':
        print("-"*30)
        findGenre()
    else:
        choice = input("Please type in 'author' or 'genre' ")

def find_author():

    matches_found = 0
    find_author = input("Type in a Author: ")
    clean_author = find_author.strip() #removes any blankspace 
    clean_author2 = clean_author.replace(".","") #removes any instance of period 

    for book in library_books:
        clean_book = book["author"].replace(".","") #replaces any instances of periods 
        if clean_author2.lower() in clean_book.lower(): 
           matches_found += 1 
           print(f"{clean_author} has {matches_found} match!")
           print(f'Book ID: {book["id"]}, Author: {book['author']}, Title: {book['title']}')
           print("-"*30)
           find_author() 
           
    if clean_author2 not in clean_book.lower():
        find_author = input("No Matches Found. \nWould you like to try again? ")
        if find_author.lower() == 'yes':
            book_search()
        elif find_author.lower() == 'no':
            print("Bringing you back to the main menu.") 
            print("Loading...")
            time.sleep(2)
            main_menu() 
        else:
            find_author = input("Please type in 'yes' or 'no'. ") 
    
def findGenre():
    matches_found = 0 
    find_genre = input("Type in a Genre: ")
    clean_genre = find_genre.strip() 

    for book in library_books:
        clean_book = book["genre"].replace("-"," ") 
        if clean_genre.lower() in clean_book.lower():
            matches_found += 1
            print(f"{clean_genre} has {matches_found} match! \nBook ID: {book["id"]}, Author: {book['author']}, Title: {book['title']}")

        elif clean_genre.lower() not in clean_book.lower():
            find_genre = input("No Matches Found. \nWould you like to try again? ")
            if find_genre.lower() == 'yes':
                findGenre()
            elif find_genre.lower() == 'no':
                print("Bringing you back to the main menu. \nLoading...")
                time.sleep(2)
                main_menu() 
            else:
                find_genre = input("Please type in 'yes' or 'no'. ")

#lvl 3 psuedocode
"""
Create a function titled checkout_book
Prompt user to enter in the book ID
Add edgecases spaces
Go through a for loop that goes through each book id
If the id is not found, prompt user to try again
If the id is found, reset the availability and due date of that book and add a count to the checkout amount 
Print when the duedate is, and thank user for using library 
"""


def checkout_book():
    book_id = input("Enter the ID of the book you wish to checkout. : ")
    clean_id = book_id.strip() 
    now = datetime.now() #variable created for the current date/time
    two_weeks = now + timedelta(weeks=2) #makes the duedate two weeks from now 

    for book in library_books:
        if clean_id.lower() in book["id"].lower():
            if book['available'] == False:
                print("This book's already been checked out.")
                #this makes sure people don't check out unavailable books.
            elif book['available'] == True:
                    book["duedate"] = two_weeks
                    book["checkouts"] +=1
                    book['available'] = False #changing the availability to False already it's been checkout
                    print('-'*30)
                    print(f"Thank you for visiting the library! \nPlease return the book by {two_weeks}. (Year-Month-Day)")


def return_book():
    book_id = input("Please enter the ID of the book you wish to return: ")
    clean_id = book_id.strip()


    for book in library_books:    
        if clean_id.lower() in book['id'].lower():
            if book["available"] == True:
                print("This book hasn't been checked out. \nDid you mean to enter a different ID?")
            elif book['available'] == False:
                print("Thank you for returning " + book['title']+"!")
                book['available'] = True
                book['duedate'] = None

#cant understand the syntax for this one, I only have the idea 
def overduebooks():
    
    for book in library_books:
        today = datetime.now()
        book_due_date = datetime.strptime(str(book['due_date']), '%Y')
        past_due = today - book_due_date
        if past_due == 1 and book['available'] == False:
            print("This is a list of all overdue books.")
            print(book['title'] + book['due_date'])



#main_menu()
#view_books()
#book_search()
#find_author
#findGenre()
#return_book()
#overduebooks()

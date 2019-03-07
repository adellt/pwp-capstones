class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        return "{name}, {email}, {n} books read".format(name=self.name, email=self.email, n=len(self.books))

    def __eq__(self, other):
        return self.email == other.email and self.name == other.name

    def get_email(self):
        #Should I change this to a string to be more pleasing or is there a reason it's like this?
        return self.email

    def change_email(self, address):
        self.email = address
        return "Your email address has been updated."

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total_rating = 0
        total_no_ratings = 0
        for rating in self.books.values():
            if rating != None:
                total_rating += rating
                total_no_ratings += 1
        average = total_rating / total_no_ratings
        return average
        #return "The average rating given by {name} is {rating}".format(name=self.name, rating=average)


class Book:
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []

    def __repr__(self):
        return "{title}, {isbn}, ${price}".format(title=self.title, isbn=self.isbn, price=self.price)

    def _eq__(self,other):
        return self.title == other.title and self.isbn == other.isbn

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self,new_isbn):
        self.isbn = new_isbn
        return "The ISBN has been updated."

    def add_rating(self,rating):
        if rating in range(0,5):
            self.ratings.append(rating)
        else:
            return "Invalid Rating. Please use a rating between 0 and 4."

    def get_average_rating(self):
        total_rating = 0
        for rating in self.ratings:
            total_rating += rating
        av_rating = total_rating / len(self.ratings)
        #print("The average rating for {book} is {rating}".format(book=self.title, rating=av_rating)
        return av_rating 
    


class Fiction(Book):
    def __init__(self, title, author, isbn, price):
        super().__init__(title, isbn, price)
        self.author = author

    def _repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

    def get_author(self):
        return self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

class TomeRater:
    def __init__(self):
        self.users = {} #eg. {email: User}
        self.books = {} #eg, {Book: number of times read}

    def __repr__(self):
        return "There are currently {books} books and {users} users in your TomeRater library.".format(books=len(self.books), users=len(self.users))
        
    def create_book(self, title, isbn, price):
        return Book(title, isbn, price)

    def input_book(self):
        title = input("Title: ")
        isbn = input("ISBN: ")
        return Book(title, isbn)

    def create_novel(self, title, author, isbn, price):
        return Fiction(title, author, isbn, price)

    def input_novel(self):
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn, price):
        return Non_Fiction(title, subject, level, isbn, price)

    def input_nonfiction(self):
        title = input("Title: ")
        subject = input("Subject: ")
        level = input("Level: ")
        isbn = input("ISBN: ")
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            user = self.users[email]
            user.read_book(book, rating)
            book.add_rating(rating)
        else:
            return "No user with email {email}".format(email=email)
        if book in self.books.keys():
            self.books[book] += 1
        else:
            self.books[book] = 1

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)
        return new_user       

    '''
    def input_user(self):
        to_check = True
        name = input("Name: ")
        email = input("Email: ")
        books = input("Books (optional): ")
        email_domains = ['.com', '.edu', '.org']

        if '@' in email:
            for domain in email_domains:
                if domain in email:
                    break
                else:
                    email = input("Please confirm your email: ")
        else:
            email = input("Please confirm your email: ")

        if email in self.users.keys():
            return "This email already exists in the system. \n {user}".format(user=self.users[email])
        else:
            self.add_user(name, email, books)
            
        return
        '''

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_read_book = []
        most_read_number = 0
        for book, value in self.books.items():
            if value == most_read_number:
                most_read_book.append(book.title)
            elif value > most_read_number:
                most_read_book = [book.title]
                most_read_number = value
            else:
                pass

        len_books = len(most_read_book)
        if len_books == 1:
            return "The most read book is {book} at {number} reads.".format(book=most_read_book[0], number=most_read_number)
        elif len_books > 1:
            return "The most read books are {books} at {number} reads.".format(books="; and ".join(most_read_book), number=most_read_number)
        else:
            return "There are no books that have been read."

        return most_read_books

    def get_n_most_read_books(self, n):
        read_books = []
        
        values = []
        for value in self.books.values():
            if value in values:
                pass
            else:
                values.append(value)
        sorted_values = sorted(values, reverse=True)

        for x in sorted_values:
            for book, value in self.books.items():
                if value == x:
                    read_books.append(book.title)
        return read_books[:n]
                

    def highest_rated_book(self):
        highest_rated_book = []
        highest_rating = 0
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating == highest_rating:
                highest_rated_book.append(book.title)
            elif rating > highest_rating:
                highest_rated_book = [book.title]
                highest_rating = rating
            else:
                pass

        len_books = len(highest_rated_book)
        if len_books == 1:
            return "The highest rated book is '{book}' at an average rating of {rating}.".format(book=highest_rated_book[0], rating=highest_rating)
        elif len_books > 1:
            return "The highest rated books are {books} at an average rating of {rating}.".format(books="; and ".join(highest_rated_book), rating=highest_rating)
        else:
            return "There are no books that have been read."

    def most_positive_user(self):
        most_positive_user = []
        highest_rating = 0
        for user in self.users.values():
            rating = user.get_average_rating()
            if rating == highest_rating:
                most_positive_user.append(user.name)
            elif rating > highest_rating:
                most_positive_user = [user.name]
                highest_rating = rating
            else:
                continue

        len_books = len(most_positive_user)
        if len_books == 1:
            return "The most positive user is {user} with an average rating of {rating}.".format(user=most_positive_user[0], rating=highest_rating)
        elif len_books > 1:
            return "The most positive users are {users} with an average rating of {rating}.".format(users="; and ".join(most_positive_user), rating=highest_rating)
        else:
            return "There are no users."

    def get_n_most_expensive_books(self, n):
        expensive_books = []
        
        prices = []
        for book in self.books.keys():
            if book.price in prices:
                pass
            else:
                prices.append(book.price)
        sorted_prices = sorted(prices, reverse=True)

        for x in sorted_prices:
            for book in self.books.keys():
                if book.price == x:
                    expensive_books.append(book.title)
        return expensive_books[:n]

    def get_worth_of_user(self, email):
        users_books = self.users[email].books
        user_name = self.users[email].name
        total_read = 0
        total_price = 0
        for book in users_books:
            total_read += 1
            total_price += book.price
        av_price = total_price / total_read
        return "The average spend of {user} is ${price}.".format(user=user_name, price=round(av_price, 2))

    
from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678, 43.00)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 27.50)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452, 76.99)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 73.37)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010, 12.88)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 120.00)
harrypotter2 = Tome_Rater.create_book("Harry Potter and the Comb of Doom", 3759435, 34.65)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)
Tome_Rater.add_book_to_user(novel2, "david@computation.org", 2)
Tome_Rater.add_book_to_user(novel2, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(harrypotter2, "alan@turing.com", 3)


print("Catalog:")
Tome_Rater.print_catalog()
print(" ")
print("Users:")
Tome_Rater.print_users()


#make sure that all books have unique ISBNs

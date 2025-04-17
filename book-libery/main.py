import os
import json

FILENAME = "./book-libery/books.json"

# This class manages book data and availability.

class Book:

    def new_book():
        title= input("Enter Book Title: ")
        while not title:
            print("Title cannot be empty.")
            title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        while not author:
            print("Author cannot be empty.")
            author = input("Enter Author Name: ")
        
        if os.path.exists(FILENAME):
            try:
                with open(FILENAME, "r") as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                print("Error reading book data. Please check the file format.")
                return
        else:
            data={}
        
        if title in data:
            print("Book already exists.")
            return
        book_id = str(len(data) + 1)
        data[book_id] = {"title": title, "author": author, "available": True}
        try:
            with open(FILENAME, "w") as file:
                json.dump(data, file)
            print(f"Book '{title}' by {author} added with ID {book_id}. ✅")
        except Exception as e:
            print(f"Error writing to file: {e}")
    
    # method for borrowing a book
    def borrow_book():
        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Error reading book data. Please check the file format.")
            return
        
        print("\nAvailable Books:")
        for book_id, book_info in data.items():
            if book_info["available"]:
                print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']} ")
                
        book_id = input("Enter the ID of the book you want to borrow: ")
        while not book_id.isdigit() or int(book_id) not in range(1, len(data) + 1):
            print("Invalid book ID.")
            book_id = input("Enter the ID of the book you want to borrow: ")
        if data[book_id]["available"]:
            data[book_id]["available"] = False
            try:
                with open(FILENAME, "w") as file:
                    json.dump(data, file)
                print(f"You have borrowed '{data[book_id]['title']}'.")
            except Exception as e:
                print(f"Error writing to file: {e}")
                return
    
    def return_book():
        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Error reading book data. Please check the file format.")
            return
        
        print("Books currently checked out: ")
        print("id \t Title")    
        for book_id, book_info in data.items():
            if not book_info["available"]:
                print(f" {book_id}. \t {book_info['title']} ")
                
        book_id=input("Input book_id you want to return: ")
        if not data[book_id]['available']:
            data[book_id]["available"] = True
            try:
                with open(FILENAME, 'w') as file:
                    json.dump(data, file)
                print(f" You have returned {data[book_id]['title']} ")
            except Exception as e:
                    print(f"Error writing to file: {e}")
            


def Menu():
    print("Welcome to the Book Library Management System")
    print("1. Add New Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. EXIT")
   

while True:
    try:
        Menu()
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            Book.new_book()
        elif choice == 2:
            Book.borrow_book()
        elif choice == 3:
            Book.return_book()
        elif choice == 4:
            print("Exiting the program. \n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")
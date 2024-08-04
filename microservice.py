# Book submission Microservice using REQ/Reply in ZMQ

import zmq
import json
import os


context = zmq.Context()
socket = context.socket(zmq.REP)

# Change socket
socket.bind("tcp:*:5555")

DATA_FILE = 'bookdata.json'


def load data():


def save data():

def add_book(user_request):

    try:
        username = user_request['username']
        new_books = user_request['books']

        book_data = load_data()

        # check for existing user, present current list
        if username in book_data:
            user_books = book_data[username]
        # If no books found for user, extend list to add new book(s)
        else:
            user_books = []

        user_books.extend(new_books)
        books_data[username] = user_books


        save_data(book_data)



    # exception
    except: Exception as e:
    return {error}
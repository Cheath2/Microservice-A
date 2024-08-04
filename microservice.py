# Book submission Microservice using REQ/Reply in ZMQ

import zmq
import json
import os


context = zmq.Context()
socket = context.socket(zmq.REP)

# Change socket as needed
socket.bind("tcp:*:5555")

DATA_FILE = 'bookdata.json'


def load_data():
    '''Function to present book data  '''
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return{}


def save_data():
    ''' Function to write data to bookdata.json'''
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)



def add_book(user_request):
    '''Add book function to present/save data by username '''
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

        # using extend here to accomodate multiple book entry additions
        user_books.extend(new_books)
        book_data[username] = user_books


        save_data(book_data)

        return{"status":"success", "message": "Book(s) added succesfully!"}

    # exception
    except Exception as e:
        return {"status":"error", "message":  f"An error has occurred: {e}."}

# Await request, respond as needed
while True:
    user_request = socket.recv_json()
    response = add_book(user_request)
    socket.send_json(response)
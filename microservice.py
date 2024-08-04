# Book submission Microservice using REQ/Reply in ZMQ

import zmq
import json
import os


context = zmq.Context()
socket = context.socket(zmq.REP)

# Change socket
socket.bind("tcp:*:5555")



def add_book(user_request):
    try:
        username = user_request['username']
        new_books = user_request['books']

        book_data = load_data()

        if username in book_data:
            user_books = book_data[username]
        else:
            user_books = []



    # exception
    except: Exception as e:
        return {error}
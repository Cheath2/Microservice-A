Book submission Microservice

This Microservice uses a REQ-Reply ZMQ pattern to allow users to add up to three books to their collection.

Book data is stored in bookdata.json.
Communication Pipe: ZMQ request/reply sockets
Currently running on local port 5555

            Actions:
'submit_books' to submit new books
'get_list' to get titles in user's data.


             References:
'Extend' Function usage referenced: https://www.geeksforgeeks.org/append-extend-python/
ZMQ usage referenced:
 Flores, Luis. Introduction to ZeroMQ. 11 June 2024.
 Req-Reply https://zguide.zeromq.org/docs/chapter1/#Ask-and-Ye-Shall-Receive


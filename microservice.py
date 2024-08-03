# Book submission Microservice

import zmq
import json
import os


context = zmq.Context()

socket = context.socket(zmq.REP)

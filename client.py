#! /usr/bin/python3

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from time import time

import generic_pb2 as gp


__author__ = "Gloire Rubambiza"
__email__ = "gbr26@cornell.edu"
__credits__ = ["Gloire Rubambiza"]

# Server's hostname
HOST = '127.0.0.1'
PORT = 8001

def prompt_infinitely(entries):
    """
        Prompts the user infinitely until they enter a valid query.
        :param entries: a list of valid entries.
    """
    user_input = None
    while user_input not in entries:
        user_input = input("Please enter a valid entry!\n")
    return user_input


def create_query():
    valid_queries = ["professor", "country", "conference", "quit", "shutdown"]
    query_type = input("Query? [professor, country, conference] : ")
    if query_type not in valid_queries:
        query_type = prompt_infinitely(valid_queries)
    query = gp.SearchRequest()
    if query_type == "professor":
        query.target = input("Please enter a professor name: ")
        query.querytype = gp.SearchRequest.DEPARTMENT
    elif query_type == "country":
        query.target = input("Please enter a country name: ")
        query.querytype = gp.SearchRequest.COUNTRY
    elif query_type == "conference":
        query.target = input("Please enter a conference name: ")
        query.querytype = gp.SearchRequest.CONFERENCE
    else:
        query.target = query_type
        query.querytype = gp.SearchRequest.CONFERENCE
    print(query.__str__())
    return query


def send_requests():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Connected to server at address %s and port %s\n" % (HOST, PORT))
        s.settimeout(10.0)
        while True:
            query = create_query()
            if query.target == "quit" or query.target == "shutdown":
                print("Sending a quit/shutdown message to server\n")
                data_bytes = query.SerializeToString()
                sent = s.send(data_bytes)
                break
            else:
                data_bytes = query.SerializeToString()
                sent = s.send(data_bytes)
                print("%s bytes sent, message is %s" % (sent, data_bytes))
                buffer = 4096
                response = gp.SearchResponse()
                payload = s.recv(buffer)
                response.ParseFromString(payload)

                # Check what is set inside the response
                response_type = response.WhichOneof("responses")
                if response_type == "faculty":
                    f_message = gp.Department()
                    f_message.CopyFrom(response.faculty)
                    print("Response: \n%s\n" % response)
                    for prof in f_message.professors:
                        print("Prof: %s\n" % prof.__str__())
                if response_type == "countries":
                    ct_message = gp.Continent()
                    ct_message.CopyFrom(response.countries)
                    print("Response: \n%s\n" % response)
                    for country in ct_message.states:
                        print("Country: %s\n" % country.__str__())
                if response_type == "conferences":
                    cf_message = gp.ACM()
                    cf_message.CopyFrom(response.conferences)
                    print("Response: \n%s\n" % response)
                    for conference in cf_message.events:
                        print("Conference: %s\n" % conference.__str__())

if __name__ == '__main__':
    send_requests()

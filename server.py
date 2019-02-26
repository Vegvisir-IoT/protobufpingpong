#! /usr/bin/python3

from socket import (socket, AF_INET, SOCK_STREAM, SOL_SOCKET,
                    SO_REUSEADDR, SHUT_RDWR)
from time import time


import generic_pb2 as gp
from util import check_query_files


__author__ = "Gloire Rubambiza"
__email__ = "gbr26@cornell.edu"
__credits__ = ["Gloire Rubambiza"]


HOST = '127.0.0.1'


#@brief: A server processing client requests using protobuf
class PingPongServer(object):
    
    def __init__(self, port):
        """
            Initialize a server instance on the port.
            :param port: An int.
        """
        self.port = port
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.port = port
        print("Server to start on port %s, address %s" % (self.port, HOST))
        self.database = {}

    def read_query_file(self, filename):
        """
            Reads a query file if it is not already cached.
            :param filename: a string.
        """
        fd = open(filename, "rb")
        details = fd.read()
        fd.close()
        return details

    def serve_for_now(self):
        """
            Continually receives messages from the wire.
        """
        try:
            self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            self.server_socket.bind((HOST, self.port))
            self.server_socket.listen(10)
            self.server_socket.setblocking(1)
        except Exception as e:
            print("Exception binding server -> %s\n" % e)
            exit(1)
        
        server_shutdown = False
        while True:
            self.connection, client_address = self.server_socket.accept()
            print("Connection established with peer %s at port %s\n\n"
                        % (client_address[0], client_address[1]))
            while True:
                query = gp.SearchRequest()
                buffer = 4096
                payload = self.connection.recv(buffer)
                query.ParseFromString(payload)
                if query.target == "quit":
                    self.handle_shutdown()
                    self.connection = None
                    break
                elif query.target == "shutdown":
                    self.handle_shutdown()
                    self.server_socket.close()
                    server_shutdown = True
                    break
                else:
                    self.dispatch_query(query)
            if server_shutdown:
                break
        print("Shutting server down...\n")
        exit(0)
    
    def handle_shutdown(self):
        """
            Shuts down the server when the client is done querying.
        """
        self.connection.shutdown(SHUT_RDWR)
        self.connection.close()
        print("Shutting down client connection..\n")

    def dispatch_query(self, query):
        """
            Dispatch the message to the right handler when received.
            :param query: A SearchRequest
        """
        print("Picking dispatcher\n")
        if query.querytype == gp.SearchRequest.DEPARTMENT:
            print("Received a professor query: \n%s\n" % query.__str__())
            if not "department" in self.database:
                dpt = gp.Department()
                data = self.read_query_file("profs.txt")
                dpt.ParseFromString(data)
                self.database['department'] = dpt
            self.handle_department_query(query)
        elif query.querytype == gp.SearchRequest.COUNTRY:
            print("Received a country query: \n%s\n" % query.__str__())
            if not "continent" in self.database:
                confs = gp.Continent()
                data = self.read_query_file("countries.txt")
                confs.ParseFromString(data)
                self.database['continent'] = confs
            self.handle_country_query(query)
        elif query.querytype == gp.SearchRequest.CONFERENCE:
            print("Received a conference query: \n%s\n" % query.__str__())
            if not "conferences" in self.database:
                continent = gp.ACM()
                data = self.read_query_file("confs.txt")
                continent.ParseFromString(data)
                self.database['conferences'] = continent
            self.handle_conference_query(query)


    def handle_department_query(self, query):
        """
            Handle a query regarding the department faculty. 
            :param query: A SearchRequest.
        """
        dept = gp.Department()
        prof_found = False
        for prof in self.database['department'].professors:
            if query.target in prof.name:
                prof_found = True
                result = dept.professors.add()
                result.name = prof.name
                result.office = prof.office
                result.email = prof.email
                result.appointment = prof.appointment
        if prof_found:
            self.send_response(dept, "dept")
        else:
            self.send_response(self.database['department'], "dept")

    def handle_country_query(self, query):
        """
            Handle a query regarding countries. 
            :param query: A SearchRequest.
        """
        continent = gp.Continent()
        country_found = False
        for country in self.database['continent'].states:
            if query.target in country.name:
                country_found = True
                result = continent.states.add()
                result.name = country.name
                result.language = country.language
                result.population = country.population
        if country_found:
            self.send_response(continent, "cont")
        else:
            self.send_response(self.database['continent'], "cont")

    def handle_conference_query(self, query):
        """
            Handle a query regarding conferences. 
            :param query: A SearchRequest.
        """
        conferences = gp.ACM()
        conference_found = False
        for conf in self.database['conferences'].events:
            if query.target in conf.name:
                conference_found = True
                result = conferences.events.add()
                result.name = conf.name
                result.location = conf.location
                result.fee = conf.fee
                result.deadline = conf.deadline
        if conference_found:
            self.send_response(conferences, "conf")
        else:
            self.send_response(self.database['conferences'], "conf")
    
    def send_response(self, response, query_type):
        """
            Sends a response to a query from the client.
            :param response: oneOf Department, ACM, Continent.
            :param query_type: A string specifying the type of query sent.
        """
        r_wrapper = gp.SearchResponse()
        if query_type == "dept":
            r_wrapper.faculty.CopyFrom(response)
            response_bytes = r_wrapper.SerializeToString()
            print("Response to be sent \n%s\n" % r_wrapper)
            self.connection.send(response_bytes)
        elif query_type == "cont":
            r_wrapper.countries.CopyFrom(response)
            response_bytes = r_wrapper.SerializeToString()
            print("Response to be sent: \n%s\n" % r_wrapper)
            self.connection.send(response_bytes)
        elif query_type == "conf":
            r_wrapper.conferences.CopyFrom(response)
            response_bytes = r_wrapper.SerializeToString()
            print("Response to be sent \n%s\n" % r_wrapper)
            self.connection.send(response_bytes)

if __name__ == "__main__":
    server = PingPongServer(8001)
    check_query_files()
    server.serve_for_now()
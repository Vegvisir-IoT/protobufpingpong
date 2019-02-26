#! /usr/bin/python3

from pathlib import Path

import generic_pb2 as gp


__author__ = "Gloire Rubambiza"
__email__ = "gbr26@cornell.edu"
__credits__ = ["Gloire Rubambiza"]

def check_query_files():
        """
            Creates query files for storing probuf objects.
        """
        files = ["profs.txt", "confs.txt", "countries.txt"]
        for f in files:
            file_exists = Path(f).is_file()
            if not file_exists:
                fd = open(f, "wb")
                if f == "profs.txt":
                    profs = {}
                    profs["John Doe"] = {'email': "johndoe@cs.cornell.edu",
                                            'office': 870,
                                            'appt': gp.Professor.ASSISTANT}
                    profs["Jane Doe"] = {'email': "janedoe@cs.cornell.edu",
                                            'office': 871,
                                            'appt': gp.Professor.ASSISTANT}
                    dept = gp.Department()
                    for prof_name, details in profs.items():
                        prof_object = dept.professors.add()
                        prof_object.name = prof_name
                        prof_object.email = details['email']
                        prof_object.office = details['office']
                        prof_object.appointment = details['appt']
                    fd.write(dept.SerializeToString())
                    fd.close()
                elif f == "confs.txt":
                    confs = {}
                    confs["SoCC 2018"] = {'location': "Carlsbad, CA", 'fee': 500, 
                                            'deadline': "05/03/2018", 
                                            'track': gp.Conference.SINGLETRACK}
                    confs["CHI 2019"] = {'location': "Glasgow, UK", 'fee': 450, 
                                            'deadline': "09/25/2018",
                                            'track': gp.Conference.TWOTRACK}
                    acm = gp.ACM()
                    for conf_name, details in confs.items():
                        event_object = acm.events.add()
                        event_object.name = conf_name
                        event_object.location = details['location']
                        event_object.fee = details['fee']
                        event_object.deadline = details['deadline']
                        event_object.track = details['track']
                    fd.write(acm.SerializeToString())
                    fd.close()
                elif f == "countries.txt":
                    countries = {}
                    countries["U.S.A"] = {'language': "English",
                                            'population': 324000000}
                    countries["Canada"] = {'language': "English/French",
                                            'population': 37000000}
                    cont = gp.Continent()
                    for country_name, details in countries.items():
                        cnt_obj = cont.states.add()
                        cnt_obj.name = country_name
                        cnt_obj.language = details['language']
                        cnt_obj.population = details['population']
                    fd.write(cont.SerializeToString())
                    fd.close()
            else:
                print("Query file %s already exists\n" % f)
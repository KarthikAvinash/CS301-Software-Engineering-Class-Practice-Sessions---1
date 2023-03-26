# Program to create a new cultural destination celebrating the heritage of India and providing a platform for emerging talents using digital technology solutions

# Requirement 1: Identify various requirements for the above program initiative that can be developed as digital solutions
# A. Online platform for artists to showcase their work
# B. Live streaming of performances and events
# C. Online ticket booking system for events
# D. Collaborative project management platform for artists and event organizers
# E. Augmented Reality (AR) and Virtual Reality (VR) technology for immersive art experiences
# F. Digital marketing and advertising platform for promoting events and artists
# Target audience: Home to Art, Artists, and the audience from India and around the world.


import json
import requests
from unittest.mock import patch

from datetime import datetime

# Make sure the api is active...


# A. Online platform for artists to showcase their work
class Artist:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description
        }

    def display(self):
        print("Artist Name: "+self.name)
        print("Artist Description: "+self.description)


class Artwork:
    def __init__(self, title, description, image_url):
        self.title = title
        self.description = description
        self.image_url = image_url

    def to_dict(self):
        print(f"{self.title}: {self.description}\nImage URL: {self.image_url}")

    def display(self):
        print("Artwork Title: "+self.title)
        print("Artwork Description: "+self.description)
        print("Artwork Image URL: "+self.image_url)

# B. Live streaming of performances and events
class Event:
    def __init__(self, name, description, date):
        self.name = name
        self.description = description
        self.date = date

    def live_stream(self):
        print(f"Live streaming {self.name} on {self.date}")

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "date": self.date
        }

    def display(self):
        print("Event Name: "+self.name)
        print("Event Description: "+self.description)
        print("Event Date: "+self.date)

# C. Online ticket booking system for events
class Ticket:
    def __init__(self, event, price):
        self.event = event
        self.price = price
        self.ticket_id = 1000

    def to_dict(self):
        return {"Ticket ID": self.ticket_id, "Event": self.event.name, "Price": self.price}

    def display(self):
        print("Ticket Id: "+str(self.ticket_id))
        print("Event on ticket: "+self.event.name)
        print("Ticket Price: "+str(self.price))


# D. Collaborative project management platform for artists and event organizers
class Project:
    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status

    def to_dict(self):
        return {"Name": self.name, "Description": self.description, "Status": self.status}

    def display(self):
        print("Project Name: "+self.name)
        print("Project Description: "+self.description)
        print("Project Status: "+self.status)


class Task:
    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status

    def to_dict(self):
        return {"Name": self.name, "Description": self.description, "Status": self.status}

    def display(self):
        print("Task Name: "+self.name)
        print("Task Description"+self.description)
        print("Task Status: "+self.status)


# E. Augmented Reality (AR) and Virtual Reality (VR) technology for immersive art experiences
class ARVR:
    def __init__(self, name, description, type):
        self.name = name
        self.description = description
        self.type = type

    def experience(self):
        print(
            f"Immersive {self.type} experience of {self.name}: {self.description}")

    def to_dict(self):
        return {"Name": self.name, "Description": self.description, "Type": self.type}

    def display(self):
        print("Immersive Art Experience Name: "+self.name)
        print("Immersive Art Experience Description: "+self.description)
        print("Immersive Art Experience Type: "+self.type)

# F. Digital marketing and advertising platform for promoting events and artists
class Promotion:
    def __init__(self, name, description, platform):
        self.name = name
        self.description = description
        self.platform = platform

    def advertise(self):
        print(f"Promoting {self.name} on {self.platform}: {self.description}")

    def to_dict(self):
        return {"Name": self.name, "Description": self.description, "Platform": self.platform}

    def display(self):
        print("Promotion Name: "+self.name)
        print("Promotion Description: "+self.description)
        print("Promotion Platform: "+self.platform)

#______________________________________________________DRIVER CODE_________________________________________
if __name__ == '__main__':
    print(":: Welcome!!\n\n")
    one = two = three = four = five = six = seven = eight = None
    print(":: Browse artists and their artworks...")
    index1 = input("Enter number between 0 and 4 to discover artists: ")
    try: 
        response = requests.get('http://127.0.0.1:5000/artist/'+str(index1))
        if response.status_code == 404:
            print("Artist not found")
        else:
            data = json.loads(response.text)
            name = data["name"]
            desc = data["description"]
            one = Artist(name, desc)
            one.display()
        print("\n")
    except:
        print("Connection refused. Please check the target api.")
    

    index2 = input("Enter number between 0 and 4 to discover artworks: ")
    try:
        response = requests.get('http://127.0.0.1:5000/artwork/'+str(index2))
        if response.status_code == 404:
            print("Artwork not found")
        else:
            data = json.loads(response.text)
            title = data["title"]
            description = data["description"]
            url = data["image_url"]
            two = Artwork(title, description, url)
            two.display()
        print("\n\n\n")
    except:
        print("Connection refused. Please check the target api.")

        
    print(":: Discover Live stream events...")
    index3 = input("Enter number between 0 and 4 to see live events: ")
    try:
        response = requests.get('http://127.0.0.1:5000/events/'+str(index3))
        if response.status_code == 404:
            print("Event not found")
        else:
            data = json.loads(response.text)
            name = data["name"]
            description = data["description"]
            date = data["date"]
            three = Event(name, description, date)
            three.display()
        print("\n\n\n")
    except:
        print("Connection refused. Please check the target api.")


    print(":: Book tickets for events...")
    index4 = input("Enter EVENT number between 0 and 4: ")
    try:
        response = requests.get('http://127.0.0.1:5000/ticket/'+str(index4))
        if response.status_code == 404:
            print("Ticket not found")
        elif three == None:
            print("No ticket as event is not chosen.")
        else:
            data = json.loads(response.text)
            id = data["Ticket ID"]
            event = data["Event"]
            price = data["Price"]
            four = Ticket(three, price)
            four.display()
        print("\n\n\n")
    except:
        print("Connection refused. Please check the target api.")



    print(":: Collaborate on projects...")
    index5 = input("Enter project number between 0 and 4: ")
    try: 
        response = requests.get('http://127.0.0.1:5000/project/'+str(index5))
        if response.status_code == 404:
            print("Project not found")
        else:
            data = json.loads(response.text)
            name = data["Name"]
            description = data["Description"]
            status = data["Status"]
            five = Project(name, description, status)
            five.display()
        print("\n")
    except:
        print("Connection refused. Please check the target api.")

    index6 = input("Enter task number between 0 and 4: ")
    try: 
        response = requests.get('http://127.0.0.1:5000/task/'+str(index6))
        if response.status_code == 404:
            print("Task not found")
        else:
            data = json.loads(response.text)
            name = data["Name"]
            desc = data["Description"]
            status = data["Status"]
            six = Task(name, desc, status)
            six.display()
        print("\n\n\n")
    except:
        print("Connection refused. Please check the target api.")
    
    print(":: Experience AR/VR...")
    index7 = input("Enter number between 0 and 4 to dicover arvr: ")
    try:
        response = requests.get('http://127.0.0.1:5000/arvr/'+str(index7))
        if response.status_code == 404:
            print("Immersive Art Experience not found")
        else:
            data = json.loads(response.text)
            name = data["Name"]
            desc = data["Description"]
            type = data["Type"]
            seven = ARVR(name, desc, type)
            seven.display()
        print("\n\n\n")
    except:
        print("Connection refused. Please check the target api.")


    print(":: Promoted events and artists...")
    index8 = input("Enter number between 0 and 4 to see promotions: ")
    try:
        response = requests.get('http://127.0.0.1:5000/promotion/'+str(index8))
        if response.status_code == 404:
            print("Promotion not found")
        else:
            data = json.loads(response.text)
            name = data["Name"]
            desc = data["Description"]
            platform = data["Platform"]
            eight = Promotion(name, desc, platform)
            eight.display()
        print("\n\n\n")
    except:
        print("Connection refused. Please check the target api.")
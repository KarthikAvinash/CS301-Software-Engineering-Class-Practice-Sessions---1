import unittest

from datetime import datetime
from unittest.mock import patch


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


promotions = [
    Promotion("Cultural Fest",
              "Celebrate the heritage of India with us", "Facebook"),
    Promotion("Music Festival",
              "Experience the soulful regional music", "Instagram"),
    Promotion("Art exhibition",
              "Witness the stunning artwork by emerging artists", "Twitter"),
    Promotion("Online auction",
              "Bid for your favorite art pieces from the comfort of your home", "Email"),
    Promotion("Art Exhibition", "Discover the beauty of contemporary art", "Twitter")]
artists = [
    Artist("Leonardo da Vinci", "Italian polymath of the Renaissance period"),
    Artist("Vincent van Gogh", "Dutch post-impressionist painter"),
    Artist("Pablo Picasso", "Spanish painter, sculptor, and printmaker"),
    Artist("Claude Monet", "French impressionist painter"),
    Artist("Salvador Dali", "Spanish surrealist artist"),
]
artworks = [
    Artwork("Mona Lisa", "A half-length portrait painting by Leonardo da Vinci",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Mona_Lisa.jpg/320px-Mona_Lisa.jpg"),
    Artwork("The Starry Night", "An oil painting by Dutch post-impressionist artist Vincent van Gogh",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/320px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"),
    Artwork("Les Demoiselles d'Avignon", "A large oil painting by Spanish artist Pablo Picasso",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Pablo_Picasso%2C_1907%2C_Les_Demoiselles_d%27Avignon%2C_oil_on_canvas%2C_243.9_x_233.7_cm%2C_Museum_of_Modern_Art.jpg/320px-Pablo_Picasso%2C_1907%2C_Les_Demoiselles_d%27Avignon%2C_oil_on_canvas%2C_243.9_x_233.7_cm%2C_Museum_of_Modern_Art.jpg"),
    Artwork("Water Lilies", "A series of approximately 250 oil paintings by French impressionist Claude Monet",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Claude_Monet_-_Water_Lilies_-_Google_Art_Project.jpg/320px-Claude_Monet_-_Water_Lilies_-_Google_Art_Project.jpg"),
    Artwork("The Persistence of Memory", "A surrealistic painting by Spanish artist Salvador Dali",
            "https://upload.wikimedia.org/wikipedia/en/thumb/6/6b/The_Persistence_of_Memory.jpg/320px-The_Persistence_of_Memory.jpg"),
]
events = [
    Event("Art Exhibition",
          "Experience the beauty of modern art at our gallery", "2023-04-15"),
    Event("Art Sale", "Buy stunning artworks at great prices", "2023-05-01"),
    Event("Artist Talk", "Join us for a talk with renowned artist John Doe", "2023-06-15"),
    Event("Art Workshop", "Learn new art techniques and skills with our experienced instructors", "2023-07-01"),
    Event("Art Auction",
          "Bid on exclusive artworks and support local artists", "2023-08-15")
]
tickets = [Ticket(events[0], 100),
           Ticket(events[1], 200),
           Ticket(events[2], 250),
           Ticket(events[3], 350),
           Ticket(events[4], 100)]
projects = [Project("Cultural Fest", "Planning the event", "In progress"),
            Project("Music Festival", "Scheduling performers", "Not started"),
            Project("Charity Drive",
                    "Organizing donation collection", "Completed"),
            Project("New Website Launch",
                    "Developing new website design", "In progress"),
            Project("Community Cleanup", "Organizing volunteers and supplies", "Not started")]
tasks = [
    Task("Create exhibit labels",
         "Write and design labels for upcoming exhibit", "In progress"),
    Task("Plan exhibit opening reception",
         "Plan the opening reception for upcoming exhibit", "To do"),
    Task("Coordinate with artists",
         "Contact artists and coordinate delivery of artwork for upcoming exhibit", "In progress"),
    Task("Update gallery brochure",
         "Design and print updated gallery brochure", "Done"),
    Task("Research new artists", "Research and recommend new artists to feature in upcoming exhibit", "To do")]
arvrs = [
    ARVR("Taj Mahal", "Explore the magnificent architecture in Virtual Reality", "VR"),
    ARVR("Ajanta Caves", "Experience the ancient rock-cut cave architecture in Augmented Reality", "AR"),
    ARVR("Great Wall of China", "Explore the iconic wall in Virtual Reality", "VR"),
    ARVR("Eiffel Tower", "Experience the Parisian landmark in Augmented Reality", "AR"),
    ARVR("Safari Adventure", "Embark on a virtual safari through African plains", "VR")]
if __name__ == '__main__':
    print(":: Welcome!!\n\n")
    one = two = three = four = five = six = seven = eight = None
    print(":: Browse artists and their artworks...")
    index1 = int(input("Enter number between 0 and 4 to discover artists: "))
    one = artists[index1]
    one.display()
    print("\n")
    index2 = int(input("Enter number between 0 and 4 to discover artworks: "))
    two = artworks[index2]
    two.display()
    print("\n\n\n")
    print(":: Discover Live stream events...")
    index3 = int(input("Enter number between 0 and 4 to see live events: "))
    three = events[index3]
    three.display()
    print("\n\n\n")
    print(":: Book tickets for events...")
    index4 = int(input("Enter EVENT number between 0 and 4: "))
    four = tickets[index4]
    four.display()
    print("\n\n\n")
    print(":: Collaborate on projects...")
    index5 = int(input("Enter project number between 0 and 4: "))
    five = projects[index5]
    five.display()
    print("\n")
    index6 = int(input("Enter task number between 0 and 4: "))
    six = tasks[index6]
    six.display()
    print("\n\n\n")
    print(":: Experience AR/VR...")
    index7 = int(input("Enter number between 0 and 4 to dicover arvr: "))
    seven = arvrs[index7]
    seven.display()
    print("\n\n\n")
    print(":: Promoted events and artists...")
    index8 = int(input("Enter number between 0 and 4 to see promotions: "))
    eight = promotions[index8]
    eight.display()
    print("\n\n\n")

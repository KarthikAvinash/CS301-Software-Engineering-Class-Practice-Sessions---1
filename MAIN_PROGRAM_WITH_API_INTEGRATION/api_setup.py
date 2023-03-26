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
import unittest
from flask import Flask, jsonify
import random
app = Flask(__name__)

# A. Online platform for artists to showcase their work

# classes:_______________________



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


class Artwork:
    def __init__(self, title, description, image_url):
        self.title = title
        self.description = description
        self.image_url = image_url

    def to_dict(self):
        return (f"{self.title}: {self.description}\nImage URL: {self.image_url}")


class Ticket:
    def __init__(self, event, price):
        self.event = event
        self.price = price
        self.ticket_id = 1000

    def to_dict(self):
        return {"Ticket ID": self.ticket_id, "Event": self.event.name, "Price": self.price}


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


class Project:
    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status

    def to_dict(self):
        return {"Name": self.name, "Description": self.description, "Status": self.status}


class Task:
    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status

    def to_dict(self):
        return {"Name": self.name, "Description": self.description, "Status": self.status}


class ARVR:
    def __init__(self, name, description, type):
        self.name = name
        self.description = description
        self.type = type

    def experience(self):
        print(
            f"Immersive {self.type} experience of {self.name}: {self.description}")

    def to_dict(self):
        print("Successful return")
        return {"Name": self.name, "Description": self.description, "Type": self.type}


class Promotion:
    def __init__(self, name, description, platform):
        self.name = name
        self.description = description
        self.platform = platform

    def advertise(self):
        print(f"Promoting {self.name} on {self.platform}: {self.description}")

    def to_dict(self):
        return {"Name": self.name, "Description": self.description, "Platform": self.platform}


# data:_______________
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
    Artist("Salvador Dali", "Spanish surrealist artist")
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



# __________END OF DATA______________________________________________________________________________________________________________


#__________________________________________________________________________artist___________________________________
@app.route('/artist/<int:index>')
def get_artist(index):
    artist = artists[index]
    return jsonify({"name": artist.name, "description": artist.description})

#__________________________________________________________________________artwork___________________________________
@app.route('/artwork/<int:index>')
def get_artwork(index):
    artwork = artworks[index]
    return jsonify({"title": artwork.title, "description": artwork.description, "image_url": artwork.image_url})

#__________________________________________________________________________events_____________________________________
@app.route('/events/<int:index>')
def get_event(index):
    if index >= 0 and index < len(events):
        return jsonify(events[index].to_dict())
    else:
        return "Event not found", 404

#__________________________________________________________________________ticket______________________________________
@app.route('/ticket/<int:index>', methods=['GET'])
def get_ticket(index):
    ticket = tickets[index]
    return jsonify(ticket.to_dict())

#__________________________________________________________________________project______________________________________
@app.route('/project/<int:index>', methods=['GET'])
def get_project(index):
    project = projects[index]
    return jsonify(project.to_dict())

#__________________________________________________________________________task___________________________________________
@app.route('/task/<int:index>', methods=['GET'])
def get_task(index):
    task = tasks[index]
    return jsonify(task.to_dict())

#__________________________________________________________________________arav_____________________________________________
@app.route('/arvr/<int:index>', methods=['GET'])
def get_arvr(index):
    arvr = arvrs[index]
    return jsonify(arvr.to_dict())

#__________________________________________________________________________promotion_________________________________________
@app.route('/promotion/<int:index>', methods=['GET'])
def get_promotion(index):
    promotion = promotions[index]
    return jsonify(promotion.to_dict())


if __name__ == '__main__':
    app.run(debug=True)

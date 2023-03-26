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

#__________________________________________TEST SCRIPTS______________________________________________
import unittest
import requests

#_______WRITTEN BEFORE_____
class IntegrationTestScript(unittest.TestCase):

    def setUp(self):
        print("In Integration Test Script SetUp... (Written Before with 5 tests)")
        self.artist = Artist('John Doe', 'A talented artist')
        self.artwork = Artwork('Mona Lisa', 'A famous painting', 'https://www.example.com/mona_lisa.jpg')
        self.event = Event('Concert', 'A music concert', datetime(2023, 5, 1))
        self.ticket = Ticket(self.event, 10)
        self.project = Project('Art Festival', 'An annual art festival', 'In progress')
        self.task = Task('Design Poster', 'Create a poster for the event', 'Not started')
        self.arvr = ARVR('Virtual Exhibition', 'A virtual art exhibition', 'Virtual Reality')
        self.promotion = Promotion('Concert Promotion', 'Promoting the concert', 'Social Media')

    def test_add_artwork_to_artist(self):
        self.artist.add_artwork(self.artwork)
        self.assertEqual(len(self.artist.artworks), 1)
        self.assertEqual(self.artist.artworks[0].title, 'Mona Lisa')

    def test_sell_ticket_for_event(self):
        self.event.live_stream()
        self.ticket_id = self.ticket.ticket_id
        self.assertEqual(self.ticket.price, 10)
        self.assertEqual(self.ticket.event.name, 'Concert')
        self.assertEqual(self.ticket.ticket_id, 1000)

    def test_artist_works_on_project(self):
        self.project.tasks = [self.task]
        self.artist.projects = [self.project]
        self.assertEqual(self.artist.projects[0].tasks[0].name, 'Design Poster')

    def test_event_uses_arvr_technology(self):
        with patch('builtins.print') as mock_print:
            self.arvr.experience()
            mock_print.assert_called_with('Immersive Virtual Reality experience of Virtual Exhibition: A virtual art exhibition')

    def test_promote_event_on_social_media(self):
        with patch('builtins.print') as mock_print:
            self.promotion.advertise()
            mock_print.assert_called_with('Promoting Concert Promotion on Social Media: Promoting the concert')


#________NEWELY WRITTEN_______
class RegressionTestScript(unittest.TestCase):
    def setUp(self):
        print("In Regression Test Script SetUp... (Written After adding API access with 8 tests)")

    def test_get_artist(self):
        response = requests.get('http://127.0.0.1:5000/artist/0')
        self.assertEqual(response.status_code, 200)
        artist_data = response.json()
        self.assertEqual(artist_data['name'], 'Leonardo da Vinci')
        self.assertEqual(artist_data['description'], 'Italian polymath of the Renaissance period')

    def test_get_artwork(self):
        response = requests.get('http://127.0.0.1:5000/artwork/0')
        self.assertEqual(response.status_code, 200)
        artwork_data = response.json()
        self.assertEqual(artwork_data['title'], 'Mona Lisa')
        self.assertEqual(artwork_data['description'], 'A half-length portrait painting by Leonardo da Vinci')
        self.assertEqual(artwork_data['image_url'], 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Mona_Lisa.jpg/320px-Mona_Lisa.jpg')
    
    def test_get_event(self):
        response = requests.get('http://127.0.0.1:5000/events/0')
        self.assertEqual(response.status_code, 200)
        event_data = response.json()
        self.assertEqual(event_data['name'], 'Art Exhibition')
        self.assertEqual(event_data['description'], 'Experience the beauty of modern art at our gallery')
        self.assertEqual(event_data['date'], '2023-04-15')
    
    def test_get_ticket(self):
        response = requests.get('http://127.0.0.1:5000/ticket/0')
        self.assertEqual(response.status_code, 200)
        ticket_data = response.json()
        self.assertEqual(ticket_data['Ticket ID'], 1000)
        self.assertEqual(ticket_data['Event'], "Art Exhibition")
        self.assertEqual(ticket_data['Price'], 100)
    
    def test_get_project(self):
        response = requests.get('http://127.0.0.1:5000/project/0')
        self.assertEqual(response.status_code, 200)
        project_data = response.json()
        self.assertEqual(project_data['Name'], 'Cultural Fest')
        self.assertEqual(project_data['Description'], 'Planning the event')
        self.assertEqual(project_data['Status'], 'In progress')
    
    def test_get_task(self):
        response = requests.get('http://127.0.0.1:5000/task/0')
        self.assertEqual(response.status_code, 200)
        task_data = response.json()
        self.assertEqual(task_data['Name'], "Create exhibit labels")
        self.assertEqual(task_data['Description'], "Write and design labels for upcoming exhibit")
        self.assertEqual(task_data['Status'], "In progress")
    
    def test_get_arvr(self):
        response = requests.get('http://127.0.0.1:5000/arvr/0')
        self.assertEqual(response.status_code, 200)
        arvr_data = response.json()
        self.assertEqual(arvr_data['Name'], 'Taj Mahal')
        self.assertEqual(arvr_data['Description'], 'Explore the magnificent architecture in Virtual Reality')
        self.assertEqual(arvr_data['Type'], 'VR')
    
    def test_get_promotion(self):
        response = requests.get('http://127.0.0.1:5000/promotion/0')
        self.assertEqual(response.status_code, 200)
        promotion_data = response.json()
        self.assertEqual(promotion_data['Name'], 'Cultural Fest')
        self.assertEqual(promotion_data['Description'], 'Celebrate the heritage of India with us')
        self.assertEqual(promotion_data['Platform'], "Facebook")


if __name__ == '__main__':
    unittest.main()

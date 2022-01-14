from .animal_requests import get_all_animals, get_single_animal
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_animals, get_single_animal
from http.server import BaseHTTPRequestHandler, HTTPServer
from views.employees_requests import get_all_employees, get_single_employee
from views.location_requests import get_all_locations, get_single_location
from views.animal_requests import create_animal

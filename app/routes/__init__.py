from flask import Flask
from .users import users_routes

def init_app(app: Flask):
    users_routes(app)

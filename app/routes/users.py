from flask import Flask
from app.controllers import users_controller


def users_routes(app: Flask):
    app.post("/users")(users_controller.create)
    app.get("/users")(users_controller.list)
    app.get("/users/<user_id>")(users_controller.retrieve)
    app.patch("/users/<user_id>")(users_controller.update)
    app.delete("/users/<user_id>")(users_controller.destroy)

from flask import request
from http import HTTPStatus as status

from app.repositories import InMemoryRepository

users_repository = InMemoryRepository()


def create():
    data: dict = request.get_json()
    user = users_repository.create(data, "uuid")


def list():
    return users_repository.find(), status.OK


def retrieve(user_id):
    user = users_repository.find_one_by(_id=user_id)
    return user, status.NOT_FOUND


def update(user_id):
    updates = request.get_json()
    updated_user = users_repository.update(user_id, updates)
    return updated_user, status.NOT_FOUND


def destroy(user_id):
    user = users_repository.delete(user_id)
    return user, status.NOT_FOUND

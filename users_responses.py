import requests

from config import base_url, post_users_body, put_users_body, post_register_body


def post_user():
    url = f'{base_url}/users'
    payload = post_users_body
    response = requests.post(url, json=payload)
    return response


def get_user(user_id):
    url = f'{base_url}/users/{user_id}'
    response = requests.get(url)
    return response


def put_user():
    url = f'{base_url}/users/2'
    payload = put_users_body
    response = requests.put(url, json=payload)
    return response


def post_register_users():
    url = f'{base_url}/register'
    response = requests.post(url, json=post_register_body)
    return response


def post_login(payload):
    url = f'{base_url}/login'
    response = requests.post(url, json=payload)
    return response


def delete_user(user_id):
    url = f'{base_url}/users{user_id}'
    response = requests.delete(url)
    return response

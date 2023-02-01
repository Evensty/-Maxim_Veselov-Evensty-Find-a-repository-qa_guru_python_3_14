from pytest_voluptuous import S

from schemas.user import new_user_schema, user_register_schema
from config import post_login_body_invalid, post_login_body, put_users_body
from users_responses import post_user, put_user, post_login, delete_user, post_register_users


class TestUsers:
    def test_post_users_check_status(self):
        response = post_user()
        assert response.status_code == 201

    def test_post_users_validate_schema(self):
        response = post_user()
        assert S(new_user_schema) == response.json()

    def test_post_register_users_check_status(self):
        response = post_register_users()
        assert response.status_code == 200

    def test_post_register_users_validate_schema(self):
        response = post_register_users()
        assert S(user_register_schema) == response.json()

    def test_put_users_check_status(self):
        response = put_user()
        data = response.json()
        name = data['name']
        job = data['job']
        assert response.status_code == 200
        assert name == put_users_body['name']
        assert job == put_users_body['job']

    def test_login_unsuccessful(self):
        response = post_login(post_login_body_invalid)
        assert response.status_code == 400

    def test_login_successful(self):
        response = post_login(post_login_body)
        data = response.json()
        token = data['token']
        assert response.status_code == 200
        assert len(token) != 0
        assert len(token) == 17

    def test_delete_users_check_status(self):
        response = delete_user(3)
        assert response.status_code == 204
















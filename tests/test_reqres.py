from pytest_voluptuous import S

from schemas.user import new_user_schema, user_register_schema
from config import post_users_body, put_users_body, post_register_body, post_login_body_invalid, post_login_body


class TestUsers:
    def test_post_users_check_status(self, reqres):
        payload = post_users_body
        response = reqres.post('/users', json=payload)
        assert response.status_code == 201

    def test_post_users_validate_schema(self, reqres):
        payload = post_users_body
        response = reqres.post('/user', json=payload)
        assert S(new_user_schema) == response.json()

    def test_post_register_users_check_status(self, reqres):
        payload = post_register_body
        response = reqres.post('/register', json=payload)
        assert response.status_code == 200

    def test_post_register_users_validate_schema(self, reqres):
        payload = post_register_body
        response = reqres.post('/register', json=payload)
        assert S(user_register_schema) == response.json()

    def test_put_users_check_status(self, reqres):
        payload = put_users_body
        response = reqres.put('/user/2', json=payload)
        data = response.json()
        name = data['name']
        job = data['job']
        assert response.status_code == 200
        assert name == put_users_body['name']
        assert job == put_users_body['job']

    def test_login_unsuccessful(self, reqres):
        payload = post_login_body_invalid
        response = reqres.post('/login', json=payload)
        assert response.status_code == 400

    def test_login_successful(self, reqres):
        payload = post_login_body
        response = reqres.post('/login', json=payload)
        data = response.json()
        token = data['token']
        assert response.status_code == 200
        assert len(token) != 0
        assert len(token) == 17

    def test_delete_users_check_status(self, reqres):
        response = reqres.delete('/users/3')
        assert response.status_code == 204
















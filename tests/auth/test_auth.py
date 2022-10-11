# from flask_login import current_user


def test_math():
    assert 20 / 5 == 4


# def test_try(client):
#     assert client.get('/home').status_code == 200
#
#
# def test_redirect(client):
#
#     response = client.get('/user', follow_redirects=True)
#     assert response.request.path == '/user/login'
#
#
# def test_login(client):
#
#     assert client.get('/user/login').status_code == 200
#     with client:
#         client.post('/user/login', data={'email': 'pupil@gmail.com', 'password': 'password123'})
#         assert current_user.is_authenticated
#
#
# def test_failed_register(client):
#
#     assert client.get('/user/register').status_code == 200
#
#     response = client.post('/user/register', data={'email': 'something@gmail.com', 'username': 'something',
#                                                    'role': 'pupil', 'password': 'password123',
#                                                    'pass_confirm': 'password321', 'agree': True}, follow_redirects=True)
#
#     assert b"Passwords must match" in response.data
#     # assert response.request.path == '/user/register'
#
#
# def test_successful_register(client):
#
#     assert client.get('/user/register').status_code == 200
#
#     response = client.post('/user/register', data={'email': 'something@gmail.com', 'username': 'something',
#                                                    'role': 'pupil', 'password': 'password123',
#                                                    'pass_confirm': 'password123', 'agree': True}, follow_redirects=True)
#
#     assert response.request.path == '/user/login'

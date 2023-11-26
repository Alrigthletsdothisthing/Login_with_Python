import requests

LoginURL = 'https://github.com/login'
AfterLogin = 'https://github.com/'
payload = {
    'Username or email address': 'your_username',
    'Password': 'your_password'
}
with requests.Session() as session:
    post = session.post(LoginURL, data=payload)
    r = session.get(AfterLogin)
    print(r.text)

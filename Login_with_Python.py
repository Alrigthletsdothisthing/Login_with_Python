import requests

LoginURL = 'https://github.com/login'
AfterLogin = 'https://github.com/'
payload = {
    'Username or email address': 'tropicalpenguin2006@icloud.com',
    'Password': 'Tinkerbell2012!!!!'
}
with requests.Session() as session:
    post = session.post(LoginURL, data=payload)
    r = session.get(AfterLogin)
    print(r.text)

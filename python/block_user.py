#!/usr/bin/python3

"""
    block_user.py
    
    MediaWiki Action API Code Samples
    Demo of `Block` module: sending POST request to block user
    MIT license
"""

import requests

S = requests.Session()

URL = "https://test.wikipedia.org/w/api.php"

# Step 1: GET Request to fetch login token
PARAMS_0 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Step 2: POST Request to log in. Use of main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
PARAMS_1 = {
    "action": "login",
    "lgname": "your_bot_username",
    "lgpassword": "your_bot_password",
    "lgtoken": LOGIN_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_1)

# Step 3: GET request to fetch CSRF token
PARAMS_2 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

# Step 4: POST request to block user
PARAMS_3 = {
    "action": "block",
    "user": "Example",
    "expiry": "2015-02-25T07:27:50Z",
    "reason": "Time out",
    "token": CSRF_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_3)
DATA = R.json()

print(DATA)

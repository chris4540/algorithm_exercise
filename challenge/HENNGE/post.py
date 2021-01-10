"""
https://www.cnblogs.com/voipman/p/6216328.html
"""
import pyotp
import time
import hashlib
import requests
import json
import base64
from requests.auth import HTTPBasicAuth


def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body))

if __name__ == '__main__':
    post_json = {
        "contact_email": "chlin3@kth.se",
        "github_url": "https://gist.github.com/chris4540/0c04030058a7c1f3f4dd74c2d6c1a64b"
    }
    secret = post_json["contact_email"] + "HDECHALLENGE003"
    userid = post_json["contact_email"]
    secretB32 = base64.b32encode(bytearray(secret,'ascii'))
    topt = pyotp.TOTP(secretB32, digits=10, digest=hashlib.sha512)

    headers = {
        'Content-type': 'application/json',
        "Host": 'admissionchallenge.example.com',
        "Accept": "*/*"}

    req = requests.Request('POST',
        'https://hdechallenge-solve.appspot.com/challenge/003/endpoint',
        data=json.dumps(post_json),
        headers=headers,
        auth=HTTPBasicAuth(userid, topt.now()))
    prepared = req.prepare()
    pretty_print_POST(prepared)
    s = requests.Session()
    # # r = requests.post(
    # #     'https://hdechallenge-solve.appspot.com/challenge/003/endpoint',
    # #     json=post_json,
    # #     headers=headers,
    # #     auth=HTTPBasicAuth(userid, topt.now()))
    r = s.send(prepared)
    print("Status code", r.status_code)
    print(r.json())


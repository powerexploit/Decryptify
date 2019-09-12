#!/usr/bin/python
# Decryptify_2.py -> Hackthebox invite code decryptor

import requests
import base64
import json

RED = '\033[31m'
END = '\033[0m'
art = RED \
    + """                                                                                                                                                                                                

 /$$$$$$$                                                      /$$     /$$  /$$$$$$          
| $$__  $$                                                    | $$    |__/ /$$__  $$         
| $$  \ $$  /$$$$$$   /$$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$   /$$| $$  \__//$$   /$$
| $$  | $$ /$$__  $$ /$$_____/ /$$__  $$| $$  | $$ /$$__  $$|_  $$_/  | $$| $$$$   | $$  | $$
| $$  | $$| $$$$$$$$| $$      | $$  \__/| $$  | $$| $$  \ $$  | $$    | $$| $$_/   | $$  | $$
| $$  | $$| $$_____/| $$      | $$      | $$  | $$| $$  | $$  | $$ /$$| $$| $$     | $$  | $$
| $$$$$$$/|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$$| $$$$$$$/  |  $$$$/| $$| $$     |  $$$$$$$
|_______/  \_______/ \_______/|__/       \____  $$| $$____/    \___/  |__/|__/      \____  $$
                                         /$$  | $$| $$                              /$$  | $$
                                        |  $$$$$$/| $$                             |  $$$$$$/
                                         \______/ |__/                              \______/ 
 
                             [++] Decryptify is Hackthebox Invite code Decryptor [++]    
                                       Contributed By: Sigmapie8 & Ankit Dobhal                                
                                         Let's Begin To hack..!            
-------------------------------------------------------------------------------
""" \
    + END
print(art)

url = "https://www.hackthebox.eu/api/invite/generate"
headers = {'User-agent': 'My User Agent 1.0'}
res = requests.post(url,headers=headers)
data = json.loads(res.text)
encoded_data = data['data']['code'].encode("utf-8")
print("Encoded code is :",encoded_data)
invite_code = base64.b64decode(encoded_data)
print("Your invite code is:",invite_code)

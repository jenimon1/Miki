import requests
import json


x = requests.get('http://127.0.0.1:8000/test2/')
a = json.loads(x.text)
db = []
count = 0

for i in a:
    
    db.append(i['fields']['user_username'])
    db.append(i['fields']['user_password'])
    #if user_enter == db[0] and password_enter == db[1]
    #to menu page
    
    print(db)
    db.clear()
    
    
    '''
    print(i['fields']['user_username'])
    print(i['fields']['user_password'])
    '''

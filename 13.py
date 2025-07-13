import requests
def  myrequests(username):
    data=requests.get(f"https://api.github.com/users/gursimran1004")

    if data.status_code == 200:
        mydata = data.json()
        print(mydata)
myrequests("fy")
import pandas as pd
import requests

r = requests.get(url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=%2B{}&inputtype=phonenumber&fields=formatted_address,name,rating&key=AIzaSyANQwyh4e_KNWOUMwLQzA5-aLZCOcdT2NU'.format(18709323151))
dat = r.json()

print(dat)

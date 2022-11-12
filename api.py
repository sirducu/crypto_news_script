import requests, json

#this api only works with certain ip adresses.
#If you found this repository, and want to use this API .. DM me on twitter @RaduFlorian85

#The script that uses this API is @SirDuCutj

r=requests.get('https://radu.ovh:8080/crypto')
all_news = r.json()

with open('news.json', 'w') as f:
    json.dump(all_news, f)
print(all_news)

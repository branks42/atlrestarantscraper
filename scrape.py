import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.com/search?cflt=restaurants&find_loc=Downtown%2C+Atlanta%2C+GA"

# Gets url
yelp_r = requests.get(url)

print(yelp_r.status_code) #200

yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')

print(yelp_soup)
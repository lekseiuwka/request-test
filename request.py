#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.daft.ie/property-for-sale/ireland?location=dublin-city&location=dun-laoghaire-dublin&location=dalkey-dublin&location=monkstown-dublin&location=sandycove-dublin&location=sandymount-dublin&salePrice_to=600000&numBeds_from=2"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

apartments=[] # a list to store quotes

table = soup.find('ul', attrs = {'data-testid':'results'})
print(table.prettify())

# for row in table.findAll('div',
# 						attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
# 	quote = {}
# 	quote['theme'] = row.h5.text
# 	quote['url'] = row.a['href']
# 	quote['img'] = row.img['src']
# 	quote['lines'] = row.img['alt'].split(" #")[0]
# 	quote['author'] = row.img['alt'].split(" #")[1]
# 	quotes.append(quote)
#
# filename = 'inspirational_quotes.csv'
# with open(filename, 'w', newline='') as f:
# 	w = csv.DictWriter(f,['theme','url','img','lines','author'])
# 	w.writeheader()
# 	for quote in quotes:
# 		w.writerow(quote)

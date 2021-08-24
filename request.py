import requests as r
from bs4 import BeautifulSoup as bs
import time

start_time = time.time()
daft = r.get('https://www.daft.ie/property-for-sale/dun-laoghaire-dublin')
soup=bs(daft.text, 'lxml')
print(soup.title.string)
print("\nThis took %s seconds." % round((time.time() - start_time),4))

start_time = time.time()
soup=bs(daft.text, 'html.parser')
print(soup.title.string)
print("\nThis took %s seconds." % round((time.time() - start_time),4))

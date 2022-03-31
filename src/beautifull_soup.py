import requests
from bs4 import BeautifulSoup
import re
URL = "https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"
# r = requests.get(URL)

content = requests.get(URL)
soup = BeautifulSoup(content.text, 'html.parser')
soup = soup.text

lst_row_url = list()
lst_text = soup.split('\n')
for x in lst_text:
    if 'src' in x:
        z = re.findall(r'https://.*ttf', x)
        lst_row_url.extend(z)
a = list(set(lst_row_url))
print('truongcl')
'  src: url(https://fonts.gstatic.com/s/nunito/v22/XRXI3I6Li01BKofiOc5wtlZ2di8HDLshRTM.ttf) format(\'truetype\');'
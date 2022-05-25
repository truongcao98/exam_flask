import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-agent':
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
}

# params = {
#     "q": "python memes",
#     "hl": "vn"
# }
string_url = """https://fonts.googleapis.com/css2?family=Bungee+Shade&display=swap
https://fonts.googleapis.com/css2?family=Gluten:wght@300;400;500;700&display=swap
https://fonts.googleapis.com/css2?family=Lobster&display=swap
https://fonts.googleapis.com/css2?family=Dosis:wght@300;400;500;700&display=swap
https://fonts.googleapis.com/css2?family=Exo:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap
https://fonts.googleapis.com/css2?family=Comfortaa:wght@300;400;500;700&display=swap
https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap
https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;700&display=swap
https://fonts.googleapis.com/css2?family=Play&display=swap
https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap
https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap
https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap
https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;500;700&display=swap
https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&display=swap
https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;700&display=swap
https://fonts.googleapis.com/css2?family=Amatic+SC:wght@400;700&display=swap
https://fonts.googleapis.com/css2?family=Rokkitt:wght@300;400;500;700&display=swap
https://fonts.googleapis.com/css2?family=Pacifico&display=swap
https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap
https://fonts.googleapis.com/css2?family=Arima+Madurai:wght@300;400;500;700&display=swap
https://fonts.googleapis.com/css2?family=Alfa+Slab+One&display=swap
https://fonts.googleapis.com/css2?family=Allura&display=swap
https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap
https://fonts.googleapis.com/css2?family=Bellota:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&display=swap
https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&display=swap
https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap
https://fonts.googleapis.com/css2?family=Fuzzy+Bubbles&display=swap
https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap"""

lst_url = list(map(str, string_url.split('\n')))
lst_row_url = list()

for URL in lst_url:
    # URL = "https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap"
    # r = requests.get(URL)

    content = requests.get(URL, headers=headers)
    content = content.text
    soup = BeautifulSoup(content, 'html.parser')
    soup = soup.text

    lst_text = soup.split('\n')
    for x in lst_text:
        if 'src' in x:
            # start = x.find('(')
            # end = x.find(')')
            # z = x[start + 1: end]
            z = re.findall('(https?:\/\/[^\s]+)\)', x)
            lst_row_url.extend(z)
a = list(set(lst_row_url))

with open('/home/truongcl/exam_flask/link.txt', 'w') as f:
    for line in a:
        f.write(line)
        f.write('\n')
print('truongcl')
'src: url(https://fonts.gstatic.com/s/nunito/v22/XRXI3I6Li01BKofiOc5wtlZ2di8HDLshRTM.ttf) format(\'truetype\');'


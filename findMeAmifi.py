# Web scraper to check the price of mifi router on jiji.ug

# from email import message

# import smtplib
import requests
from bs4 import BeautifulSoup

# get price function
def get_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find('meta', {'property': 'product:price:amount'})['content']
    return price

# add price functions
def add_prices(p1, p2, p3):
    total = (float(p1) + float(p2) +float(p3))
    return total

# email sending function
# def send_mail():
#     server = smtplib.SMTP('smtp.gmail', 587)
#     server.starttls()
#     server.login('you@gmail.com', 'password')
#     subject = 'Tour price today'
#     body = f'The price for the mifi is {mifi_price}'
#     message = f''
#     server.sendmail('emailfrom@gmail.com','emailto_@gmail.com', message)
#     print('Email sent')
#     server.quit()


# mifi_price = get_price('https://jiji.ug/central-division/other-services/mtn-broadband-mifis-kWJwRvPLhZG1QybTwgpL4PTb.html?page=1&pos=10&cur_pos=10&ads_per_page=20&ads_count=74&lid=1kwUlAsLIwbV5sTt')

print('Mifi Price in UGX'+ get_price('https://jiji.ug/central-division/other-services/mtn-broadband-mifis-kWJwRvPLhZG1QybTwgpL4PTb.html?page=1&pos=10&cur_pos=10&ads_per_page=20&ads_count=74&lid=1kwUlAsLIwbV5sTt'))

# print(add_prices())

# send_mail()

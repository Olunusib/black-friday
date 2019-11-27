import requests
from bs4 import BeautifulSoup
import smtplib
from twilio.rest import Client
import time

URL = 'https://shop.simplemobile.com/shop/en/simplemobile/phones/sm-iphone-6s-plus-32gb'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}


def price_check():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(name=None, attrs={
        'class': 'price top-push-6',
    }).get_text()
    real_price = float(price[1:-2] + '.99')
    print('Current Price Is: ' + str(real_price))
    if real_price < 155:
        sendmail()
        send_text()

#Define the sendmail function
def sendmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('youremail@gmail.com', 'yourapppassword')
    subject = 'The iphone 6s has fallen!'
    body = 'Check it out! https://shop.simplemobile.com/shop/en/simplemobile/phones/sm-iphone-6s-plus-32gb'
    message = f"Subject:{subject}\n\n{body}"
    server.sendmail('FromThisEmail@gmail.com', 'ToThisEmail@gmail.com', message)
    print('Email Sent!')
    server.quit()

#Define the send_text function
def send_text():
    client = Client("YourTwilioID", "YourTwilioAuthToken")
    client.messages.create(to="YourPhoneNumber",
                           from_="TwilioNumber",
                           body="The iphone 6s has fallen! \n\n Check it out! "
                                "https://shop.simplemobile.com/shop/en/simplemobile/phones/sm-iphone-6s-plus-32gb")
    print('Text Sent!')

#Checks every hour.
while True:
    price_check()
    time.sleep(3600)

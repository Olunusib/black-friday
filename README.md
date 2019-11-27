# black-friday
Black Friday with Python. Monitor your favorite item's price online this season. <br>
SMS and Enail notifications if there's any price change. <br>
Get those 'fastest finger' deals first.


How it wroks:
- You can use this script on any website as long as you can extract an item's price using BeautifulSoup.
- For this script, we are monitoring the iphone 6s plus at https://shop.simplemobile.com/shop/en/simplemobile/phones/sm-iphone-6s-plus-32gb
- The price is currently at $199.99 and is expected to come around $149.99 in a fastest finger deal.
- The script checks the price of the phone every hour (You can change this) and checks if theres a change in price yet.
- Once there's a change, email and SMS alerts are triggered and sent to you with a customised message and its link.


Tools to have:
- You need to have a [twilio](https://www.twilio.com/referral/Q1X0Aa) account (free or paid) for the SMS service.
- You need to have a google App Password and 2FA configured on your device for the email service (The most secure way).

Screeenshots:

<img src='https://github.com/Olunusib/black-friday/blob/master/unnamed%20(1).jpg'>
<img src='https://github.com/Olunusib/black-friday/blob/master/unnamed.jpg'>

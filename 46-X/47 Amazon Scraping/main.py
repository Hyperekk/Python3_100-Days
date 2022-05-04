import requests
from bs4 import BeautifulSoup
import smtplib, ssl
from email.mime.text import MIMEText

LINK = "https://www.amazon.com/dp/B000VA48PM/ref=sbl_dpx_kitchen-electric-cookware_B0053WRWX8_0"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
    "Accept-Language": "pl,en;q=0.9,en-GB;q=0.8,en-US;q=0.7"
}

response = requests.get(url=LINK,headers=HEADERS)
soup = BeautifulSoup(response.text,"lxml")

#Getting price
prices_tags = soup.find(name="span", class_="a-price a-text-price a-size-medium apexPriceToPay")
prices = [price.getText() for price in prices_tags]
price = float(prices[0].split("$")[1])

#Getting product name
product_name = soup.find(name="span", id="productTitle").get_text().strip()

#Sending mail
text = f""""The product you were searching for: {product_name} is now ${price} \n
Link: {LINK}"""

msg = MIMEText(text)
msg['Subject'] = "Price Alert!"
msg['From'] = input("Your mail: ")
msg['To'] = input("Receiver's mail: ")

port = 465
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("kurkiewicz.maciej2@gmail.com", password)
        server.sendmail("kurkiewicz.maciej2@gmail.com", "kurkiewicz.maciej12@gmail.com", msg.as_string())
        server.quit()
except:
    print("There was an Error (¬_¬ )")

else:
    print("Message sent succesfully!! ☜(ﾟヮﾟ☜)")
from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.environ["EMAIL_ADDRESS"]
my_password = os.environ["EMAIL_PASSWORD"]
product_link = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "bg-BG,bg;q=0.9,en;q=0.8",
    "Dnt": "1",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
  }

response = requests.get(product_link, headers= headers)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
# print(soup.prettify())
item = soup.find("span", class_="a-offscreen")
item_price = float(item.getText().split("$")[1])
# print(item_price)

title = soup.find(id="productTitle").get_text().split()
item_title = "".join(title)
# print(item_title)
if item_price <= 100:
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"]) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Amazon Price Alert!\n\n{item_title}is now at ${item_price}\n {product_link}".encode("utf-8"))

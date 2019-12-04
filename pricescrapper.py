import requests

from bs4 import BeautifulSoup
import smtplib

url= 'https://www.amazon.in/Samsung-EO-BG920BBEGIN-Bluetooth-Headphones-Black-Sapphire/dp/B01A31SHF0/ref=lp_17408712031_1_6?s=electronics&ie=UTF8&qid=1575471620&sr=1-6'  #the needed URL

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}

def check_price():
    page= requests.get(url, headers=headers)

    soup1=BeautifulSoup(page.content, 'html.parser')

    soup2=BeautifulSoup(soup1.prettify(),"html.parser")

    #print(soup.prettify())

    title=soup2.find(id='productTitle').get_text()

    print(title.strip())

    price=soup2.find(id='priceblock_ourprice').get_text()

    print(price)

    converted_price=float(price[1:5])  #The problem occurs here


    wanted_price=3,000  #the price u need
    if(converted_price<=3,000):
        print("starting mail service")
        sendmail()



def sendmail():
    
    #The username and password  are removed and should be added before execution

    username='sender email'
    password='sender password'
    subject="price fell down"

    content='The price has decreased'
    msg= f'Subject:{subject}\n\n{content}'

    #init gail SMTP
    mail= smtplib.SMTP('smtp.gmail.com',587)

    #identify to server

    mail.ehlo()

    #encrypt session
    mail.starttls()

    #login
    mail.login('username','password')

    #send message
    mail.sendmail('Sender email ','Reciever email',msg)

    #end mail connection 
    mail.close()

    print('Email Sent')




check_price()
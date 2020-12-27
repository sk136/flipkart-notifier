from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as expc
from bs4 import BeautifulSoup
from datetime import datetime
import os
import time
import requests


def discord():
    global i,msg_count
    if name.text.startswith('Delivery'):
        i=i+1
        if i<=msg_count:
            discord_webhook_url = 'WEBHOOK URL (Str Type)'
            Message = {"content": name.text}
            requests.post(discord_webhook_url, data=Message)
            time.sleep(1.5)
            print('Message sent to Discord\n')
        else:
            driver.quit()
            exit()  

def pincode():
    WebDriverWait(driver, 10).until(expc.presence_of_element_located((By.ID, "pincodeInputId")))
    element = driver.find_element_by_id('pincodeInputId')
    element.send_keys(pin)
    element.send_keys(Keys.RETURN)
    time.sleep(8)
    
def outofstock():
    while True:
        try: 
            driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button')
            break
        except:
            p=driver.find_element_by_class_name('_16FRp0')
            now = datetime.now()
            current_time = now.strftime("%H:%M  ")
            print(current_time,end='')
            print('%s\n'%p.text)
        driver.refresh()
        time.sleep(20)
            
        
#Initialising chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

chrome_driver = os.getcwd() +"\\chromedriver.exe"

#Enter the Picode
pin='PINCODE HERE (Str Type)'

driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())

#Initialising driver and Enter URL of Page
driver.get('URL HERE')

outofstock()
pincode()

i=0
#Enter the COUNT here (INT type)(Default 3)
msg_count= 3

while(True):
    driver.refresh()
    
    #Enter Refresh Frequency (INT TYPE)(Default 5)
    frqy= 5  
    time.sleep(frqy)
    
    c=driver.page_source
    soup = BeautifulSoup(c,features="lxml")
    name=soup.find('div', attrs={'class':'_1NQ_ER'})  
    if name== None:
       name=soup.find('div', attrs={'class':'_3XINqE'})

    now = datetime.now()
    current_time = now.strftime("%H:%M  ")
    print(current_time,end='')
    print(name.text)
    
    discord()
    

#ATTENTION
#I'm not responsible for any loss or damage caused to you
#YOU ARE USING THIS SCRIPT ON YOUR OWN RISK

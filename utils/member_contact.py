from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# concurrent 
import time 
import csv
from itertools import islice
import pandas as pd 




# driver = webdriver.Chrome()
#banned 
# email = "8208600148" 
# password = "8983831874"

email = "9356459379"
password = "9588434875"

# # Example: Open Google in the specific Chrome profile
# driver.get("https://www.facebook.com")
# time.sleep(100)
# # Perform your Selenium actions here

# # Close the browser
# driver.quit()



option = Options()
option.add_argument("--headless=new")
option.add_argument("--disable-infobars")
# option.add_argument(f'--proxy-server=190.114.253.210:3389')
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--disable-notifications")
option.add_experimental_option('excludeSwitches', ['enable-logging'])


# driver  = webdriver.Chrome(options=option)

# url = 'https://www.facebook.com/'
# # request_url = requests.get(url)

# driver.get(url)
# time.sleep(1)

# username_field = driver.find_element(By.NAME, 'email')
# username_field.send_keys(email)
# password_field = driver.find_element(By.NAME, 'pass')
# password_field.send_keys(password)
# login_button = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
# login_button.click()
# time.sleep(15)
# print("logged in")


def get_email_phone(file_name):
    # members = pd.read_csv(file_name)    
    # print(len(members))
    # members = csv.reader(open(file_name, "r", encoding="utf-8"))
    with open("csv/wecomforum(7000).csv", "r", encoding="utf-8") as read_file:
        reader = csv.reader(read_file)
        members = [mem for mem in reader]
        # for mem in islice(members, 10):
        #     print(mem)

    # print(members)
    # print("total members : ", len(members)) 
    # with open("csv_email/wecomforum.csv", "r", encoding="utf-8") as write_file:
    #     writer = csv.writer()
    for mem in members[1:10]:
        url = mem[1]
        print("url : ", url)
        user_id = url.split("/")[-2]
        base_url = f"https://www.facebook.com/profile.php?id={user_id}&sk=about_contact_and_basic_info"
        print("facebook url : ", base_url)


get_email_phone(file_name="csv/wecomforum(7000).csv")

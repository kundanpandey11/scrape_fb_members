from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# concurrent 
import time 
import csv




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


driver  = webdriver.Chrome(options=option)

url = 'https://www.facebook.com/'
# request_url = requests.get(url)

driver.get(url)
time.sleep(1)

username_field = driver.find_element(By.NAME, 'email')
username_field.send_keys(email)
password_field = driver.find_element(By.NAME, 'pass')
password_field.send_keys(password)
login_button = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
login_button.click()
time.sleep(15)
print("logged in")

def save_members(group_url="https://www.facebook.com/groups/DSEntrepreneurs/members", output_file="DSEntrepreneurs.csv"):
    driver.get(group_url)
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)
    container_count = 2
    scroll_count = 1
    member_list = []
    attempt = 0 
    exception = ""
    while True:
        try: 
            mem = driver.find_element(By.XPATH, f"*//div[@style='padding-left: 8px; padding-right: 8px;'][{container_count}]")
            # print(mem.text)
            try:
                name = mem.find_element(By.XPATH, ".//div[@class='xu06os2 x1ok221b']").text
                url = mem.find_element(By.XPATH, ".//div[@class='xu06os2 x1ok221b']//a").get_attribute('href')
            except Exception as e: 
                # print(e)
                name = url = ""
            try:
                joined = mem.find_element(By.XPATH, ".//div[@class='xu06os2 x1ok221b'][2]").text
            except Exception as e:
                # print(e)
                joined = "" 
            try: 
                work_post = mem.find_element(By.XPATH, ".//div[@class='xu06os2 x1ok221b'][3]").text
            except Exception as e:
                # print(e)
                work_post = ""
            data = [name, url, joined, work_post]
            # print(data, container_count)
            member_list.append(data)
            attempt = 0
            container_count += 1
        except Exception as e:
            exception = e
            print("Scrolling....")
            # for i in range(4):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
            scroll_count += 1
            attempt += 1
        if container_count % 100 == 0:
            print(data, container_count)
        
        if attempt == 5:
            print("sleeping for 5 minutes")
            print(exception)
            time.sleep(200)
        if attempt == 10: 
            print(exception)
            break


        with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
    
            # Write each row in the list to the CSV file
            for row in member_list:
                csv_writer.writerow(row)
     
save_members()


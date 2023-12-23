from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# concurrent 
import time 
import csv




# driver = webdriver.Chrome()
email = "8208600148" 
password = "8983831874"

# # Example: Open Google in the specific Chrome profile
# driver.get("https://www.facebook.com")
# time.sleep(100)
# # Perform your Selenium actions here

# # Close the browser
# driver.quit()



option = Options()
option.add_argument("--headless=new")
option.add_argument("--disable-infobars")
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

def save_group_members(group_url="https://www.facebook.com/groups/DSEntrepreneurs/members", group_name="DSEntrepreneurs.csv"):
    print("logged in")
    driver.get(group_url)
    time.sleep(10)
    for i in range(100):
    
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
    main_container = driver.find_element(By.XPATH, "//div[@class='x1wsgfga']/div/div")
    # member_div = main_container.find_elements(By.XPATH, "//div[@class='x1oo3vh0 x1rdy4ex']")
    member_div = main_container.find_elements(By.XPATH, "//div[@role='listitem']")
    # print(member_div)
    
    print("total members found : ", len(member_div))
    member_list = []
    for mem in member_div:
        try:
            name = mem.find_element(By.XPATH, ".//div[@class='xu06os2 x1ok221b']").text
        except Exception as e :
            print(e)
            name = ""
        try: 
            # print(name)
            url = mem.find_element(By.XPATH, ".//div[@class='xu06os2 x1ok221b']//a").get_attribute('href')
        except Exception as e:
            print(e)
            url = ""
        try: 
            joined = mem.find_element(By.XPATH, ".//div[@class='xu06os2 x1ok221b'][2]").text
        except Exception as e:
            print(e)
            joined = ""   
        try: 
            work_post = mem.find_element(By.XPATH, ".//div[@class='xu06os2 x1ok221b'][3]").text
        except Exception as e:
            print(e)
            work_post = ""
        print(name, url, joined, work_post)
        data = [name, url, joined, work_post]
        member_list.append(data)
        print()
        
    with open(group_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
    
        # Write each row in the list to the CSV file
        for row in member_list:
            csv_writer.writerow(row)
     



save_group_members()
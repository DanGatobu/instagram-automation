from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time as tt
usern='c.ar.lover'
password1='dannewton2002'
def login(username,password):
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")


    tt.sleep(10)

# Find the username input element using XPath

    username_element = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')


# Input the username
    username_element.send_keys(username)    

    passelement=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
    passelement.send_keys(password)
    login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
    login_button.click()
    tt.sleep(5)
    # element = WebDriverWait(driver, 10).until(
    # EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))

# Perform actions on the element
    # element.click()
    ntnow=driver.find_element(By.XPATH,"//*[text()='Not Now']")  
    ntnow.click()
    tt.sleep(5)# clicking 'not now btn'
    # driver.find_element((By.XPATH,"//button [contains(text(), 'Not Now')]")).click()
    # tt.sleep(10)
    pf=driver.find_element(By.XPATH,'//*[@id="mount_0_0_gT"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[6]/div/span/div/a')
    pf.click()
    tt.sleep(20)

# Wait for a few seconds to see the result (you might need to adjust the time based on the actual loading time)
# tt.sleep(60)
login(usern,password1)
def postpicture():
    
    pass
# Close the browser window
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import re
import time as tt
import datetime
import random


def extract_and_convert_date(input_string):
    # Define a regex pattern to match the date format
    date_pattern = re.compile(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b')

    # Find the date pattern in the input string
    match = date_pattern.search(input_string)

    if match:
        # Extract the matched date string
        date_string = match.group(0)

        # Convert the date string to a datetime object
        date_object = datetime.datetime.strptime(date_string, '%B %d, %Y')
        # print(date_object)

        return date_object
    
    
def login(driver,username, password):

    driver.get("https://www.instagram.com/accounts/login/")

    # Find the username input element using XPath
    username_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
    )

    # Input the username
    username_element.send_keys(username)

    # Find the password input element using XPath
    passelement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))
    )
    
    # Input the password
    passelement.send_keys(password)

    # Find the login button and click it
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button'))
    )
    login_button.click()

    try:
        # Handle "Save Password" pop-up
        not_now_xpath = "//div[@role='button' and text()='Not now']"
        not_now_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, not_now_xpath))
        )
        not_now_button.click()
    except:
        pass  # Ignore if "Not now" button is not found

    try:
        # Handle notification pop-up
        not_now_notification_xpath = "//button[text()='Not Now']"
        not_now_notification_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, not_now_notification_xpath))
        )
        not_now_notification_button.click()
    except:
        pass  # Ignore if "Not Now" button for notifications is not found
    
    
def postpicture(driver,url_link, caption='wow'):
    # Find the New Post SVG element
    svg_xpath_expression = "//*[local-name()='svg' and @aria-label='New post']"
    new_post = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, svg_xpath_expression))
    )
    new_post.click()
    sv = "//span[text()='Post']"
    new_post = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, sv))
    )
    new_post.click()

    # Wait for the Select from computer button and click it
    button_xpath_expression = "//button[text()='Select from computer']"
    select_button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, button_xpath_expression))
    )
    select_button_element.click()

    # Write the URL and press Enter
    tt.sleep(3)  # You can use a small sleep here if needed
    pyautogui.write(url_link)
    pyautogui.press('enter')

    # Wait for the Select Crop button and click it
    crop_xpath = "//*[local-name()='svg' and @aria-label='Select crop']"
    select_crop = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, crop_xpath))
    )
    select_crop.click()
    outline = "//*[local-name()='svg' and @aria-label='Photo outline icon']"
    outline = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, outline))
    )
    outline.click()


    # Wait for the Next button and click it
    next_exp = "//div[@role='button' and text()='Next']"
    next_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, next_exp))
    )
    next_icon.click()
    
    nex = "//div[@role='button' and text()='Next']"
    nex = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, nex))
    )
    nex.click()
    tt.sleep(7)
    captionexpression = "//div[@role='textbox' and @aria-label='Write a caption...']"
    caption_element = driver.find_element(By.XPATH, captionexpression)
    caption_element.send_keys(caption)
    tt.sleep(3)


    # Wait for the Share button and click it
    share_expression = "//div[text()='Share']"
    share_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, share_expression))
    )
    share_element.click()

    # Wait for the Close SVG element and click it
    tt.sleep(10)
    close_pop = "//*[local-name()='svg' and @aria-label='Close']"
    
    
    action=ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH, close_pop)).click().perform()
    tt.sleep(15) 
    
    
def home(driver):
    home_btn = "//*[local-name()='svg' and @aria-label='Home' and @role='img']"
    home_btn_element = driver.find_element(By.XPATH, home_btn)
    home_btn_element.click()

    tt.sleep(7)   
    
def scroll(driver):
        # Find elements after scrolling
    follb = driver.find_elements(By.XPATH, "//div[text()='Following']")
    if len(follb) == 0:
        follb = driver.find_elements(By.XPATH, "//div[text()='Follow']")

    # Check if there are elements to scroll to
    if len(follb) > 1:
        i = follb[-2]

        actions = ActionChains(driver)
        scroll_origin = ScrollOrigin.from_element(i)
        actions.scroll_from_origin(scroll_origin, 0, 400).perform()
        tt.sleep(3)
def fp(driver):
    follow_buttons = driver.find_elements(By.XPATH, "//div[text()='Follow']")
       
    for button in follow_buttons:
        button.click()
        tt.sleep(2)
    try:
            # Check for the pop-up and handle it
            popup_xpath = "//div[contains(text(), 'OK')]"
            popup_element = driver.find_element(By.XPATH, popup_xpath)
            popup_element.click()
            tt.sleep(2)
    except NoSuchElementException:
            # No pop-up, continue with other actions
            pass
        
def user_profile(driver,username):
    profile_picture_alt = f"{username}'s profile picture"

    xpath_expression = f"//img[contains(@alt, \"{profile_picture_alt}\")]"
    image_element = driver.find_element(By.XPATH, xpath_expression)
    image_element.click()
    tt.sleep(10)
  
def follow(driver,profile):
    try:
        # Use WebDriverWait to wait for the presence of the search button
        search_btn = "//*[local-name()='svg' and @aria-label='Search' and @role='img']"
        search_btn_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_btn))
        )
        search_btn_element.send_keys(profile)
        tt.sleep(7)
        search_btn_element.send_keys(Keys.ENTER)
    except:
        pass

    try:
        search_btn_element.click()
        # Use WebDriverWait to wait for the presence of the search input element
        input_xpath_expression = "//input[@aria-label='Search input' and @placeholder='Search']"
        search_input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, input_xpath_expression))
        )
        search_input_element.send_keys(profile)
        tt.sleep(6)
        search_input_element.send_keys(Keys.ENTER)
        tt.sleep(8)

        # Use WebDriverWait to wait for the presence of the profile span element
        span_xpath_expression = f"//span[contains(text(), '{profile}')]"
        span_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, span_xpath_expression))
        )
        span_element.click()
        tt.sleep(10)
        
        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        tt.sleep(5)
    except:
        pass

    image_xp = f"//img[contains(translate(@alt, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{profile.lower()}')]"
    image_element = driver.find_elements(By.TAG_NAME, 'img')
    aggw_div = driver.find_elements(By.XPATH, image_xp)

    image_info_list = []

    for image_element in image_element:
        src = image_element.get_attribute('src')
        alt = image_element.get_attribute('alt')

        if 'profile' in alt.lower():
            continue

        dateobj = extract_and_convert_date(alt)
        if dateobj is not None:
            image_info_list.append({
                'src': src,
                'alt': alt,
                'date': dateobj
            })

    most_recent_image = max(image_info_list, key=lambda x: x['date'])

    image_xp = f"//img[contains(@src, '{most_recent_image['src']}')]"

    # Use WebDriverWait to wait for the visibility of the most recent image element
    most_recent_image_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, image_xp))
    )

    # Click on the most recent image
    parent_container = most_recent_image_element.find_element(By.XPATH, './ancestor::div[@class="_aagu"]')
    
    # Use WebDriverWait to wait for the element to be clickable
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, image_xp))
    )

    # Click on the parent container
    parent_container.click()
    tt.sleep(7)

    liked_element = driver.find_element(By.XPATH, "//a[contains(@href, 'liked_by')]")
    liked_element.click()
    tt.sleep(7)

    counter=0
    while counter<3:
        follow_buttons = driver.find_elements(By.XPATH, "//div[text()='Follow']")
        if len(follow_buttons)<1:
            scroll(driver)
            counter+=1
            continue
        else:
            if counter>0:
                counter=0
            fp(driver)
    
    # Use WebDriverWait to wait for the presence of the Close SVG element
    close_pop="//*[local-name()='svg' and @aria-label='Close' and @role='img']"
    
    action=ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH, close_pop)).click().perform()
    tt.sleep(2)
    close_pop="//*[local-name()='svg' and @aria-label='Close' and @role='img']"
    # driver.find_element(By.XPATH, close_pop).click()
    action.move_to_element(driver.find_element(By.XPATH, close_pop)).click().perform()
    

def ufbtn(driver):
    
    follow_buttons = driver.find_elements(By.XPATH, "//div[text()='Following']")
    rv=len(follow_buttons)
    for i,button in enumerate(follow_buttons):
        if i==0:
            continue
        button.click()
        
        tt.sleep(2)
        unfollow_button = driver.find_element(By.XPATH, "//button[text()='Unfollow']")
        unfollow_button.click()
        tt.sleep(3)
    try:
            # Check for the pop-up and handle it
            popup_xpath = "//div[contains(text(), 'Ok')]"
            popup_element = driver.find_element(By.XPATH, popup_xpath)
            popup_element.click()
            tt.sleep(2)
    except NoSuchElementException:
            # No pop-up, continue with other actions
            pass
        
    return(rv)

def unfollow(driver,lim, username):
    home(driver)
    tt.sleep(8)
    user_profile(driver,username)
    
    # Use WebDriverWait to wait for the presence of the 'following' link
    fobtn = "//a[contains(@href, 'following')]"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, fobtn))
    ).click()

    tt.sleep(5)

    
    counter = 0
    l = 0
    while counter < 3 and l < lim:
        follow_buttons = driver.find_elements(By.XPATH, "//div[text()='Following']")
        if len(follow_buttons) < 1:
            scroll(driver)
            counter += 1
            continue
        else:
            if counter > 0:
                counter = 0
            li = ufbtn(driver)
            l += li
    try:
        ufbtn(driver)
    except:
        pass

    # Use WebDriverWait to wait for the presence of the Close SVG element
    close_pop="//*[local-name()='svg' and @aria-label='Close' and @role='img']"
    
    action=ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH, close_pop)).click().perform()
    tt.sleep(2)



# def comb(lim,username,profile,password,link):
#     login(profile,password)
#     action = random.choice(["follow", "unfollow","post"])

#     if action == "follow":
#         follow(lim, username)
#     elif action == "unfollow":
#         unfollow(profile)
#     elif action == "post":
#         postpicture(link)

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
usern=''
password1=''
driver = webdriver.Chrome()

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
def login(username,password):
    
    driver.get("https://www.instagram.com/accounts/login/")


    tt.sleep(3)

# Find the username input element using XPath

    username_element = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')


# Input the username
    username_element.send_keys(username)    

    passelement=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
    passelement.send_keys(password)
    login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
    login_button.click()
    tt.sleep(10)
    # element = WebDriverWait(driver, 10).until(
    # EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
    try:
        # Handle "Save Password" pop-up
        not_now_xpath =  "//div[@role='button' and text()='Not now']"
        not_now_button = driver.find_element(By.XPATH, not_now_xpath)
        not_now_button.click()
        tt.sleep(10)
    except:
        pass  # Ignore if "Not now" button is not found

    try:
        # Handle notification pop-up
        not_now_notification_xpath = "//button[text()='Not Now']"
        not_now_notification_button = driver.find_element(By.XPATH, not_now_notification_xpath)
        not_now_notification_button.click()
    except:
        pass  # Ignore if "Not Now" button for notifications is not found

    tt.sleep(15)
    # driver.find_element((By.XPATH,"//button [contains(text(), 'Not Now')]")).click()
    # tt.sleep(10)
    # pf=driver.find_element(By.XPATH,'//*[@id="mount_0_0_gT"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[6]/div/span/div/a')
    # pf.click()
    # Example using a link containing part of the username in its text content
    # link_selector =  f"//a[contains(text(), '{username}')]"
    # link_element = driver.find_element(By.XPATH, '//*[@id="mount_0_0_gT"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[6]/div/span/div/a/div')#link_selector)
    # profile_picture_alt = f"{username}'s profile picture"

    # xpath_expression = f"//img[contains(@alt, \"{profile_picture_alt}\")]"
    # image_element = driver.find_element(By.XPATH, xpath_expression)
    # image_element.click()

    # tt.sleep(8)

# Wait for a few seconds to see the result (you might need to adjust the time based on the actual loading time)
# tt.sleep(60)
login(usern,password1)
imagurl = r"D:\downloads\newdownload\pexels-mike-bird-112460.jpg"

cap='wow'
def postpicture(url_link,caption):
    svg_xpath_expression = "//*[local-name()='svg' and @aria-label='New post']"
    new_post = driver.find_element(By.XPATH, svg_xpath_expression)
    new_post.click()
    tt.sleep(5)
    span_xpath_expression = "//span[text()='Post']"
    post_span_element = driver.find_element(By.XPATH, span_xpath_expression)
    post_span_element.click()
    tt.sleep(5)
    # Find button by text
    button_xpath_expression = "//button[text()='Select from computer']"
    select_button_element = driver.find_element(By.XPATH, button_xpath_expression)
    select_button_element.click()
    tt.sleep(7)
    pyautogui.write(url_link) 
    tt.sleep(7)
    pyautogui.press('enter')
    tt.sleep(7)
    crop_xpath = "//*[local-name()='svg' and @aria-label='Select crop']"
    select_crop = driver.find_element(By.XPATH, crop_xpath)
    select_crop.click()
    tt.sleep(7)
    # Find the <svg> element by local name and aria-label
    orgin_size = "//*[local-name()='svg' and @aria-label='Photo outline icon']"
    photo_outline = driver.find_element(By.XPATH, orgin_size)
    photo_outline.click()
    tt.sleep(7)
    next_exp = "//div[@role='button' and text()='Next']"
    next_icon = driver.find_element(By.XPATH, next_exp)
    
    next_icon.click()
    
    tt.sleep(7)
    next_button= "//div[@role='button' and text()='Next']"
    next_element = driver.find_element(By.XPATH, next_button)
    next_element.click()
    tt.sleep(7)

    # Find the <div> element for writing a caption by class and text content
    captionexpression = "//div[@role='textbox' and @aria-label='Write a caption...']"
    caption_element = driver.find_element(By.XPATH, captionexpression)
    caption_element.send_keys(caption)
    tt.sleep(3)
    share_expression = "//div[text()='Share']"
    share_element = driver.find_element(By.XPATH, share_expression)

    share_element.click()
    tt.sleep(15)
    close_expression = "//*[local-name()='svg' and @aria-label='Close']"
    close_element = driver.find_element(By.XPATH, close_expression)

# Perform an action on the Close <svg> element
    close_element.click()
    

    tt.sleep(15)

# postpicture(imagurl,cap)
tt.sleep(3)
def home():
    home_btn = "//*[local-name()='svg' and @aria-label='Home' and @role='img']"
    home_btn_element = driver.find_element(By.XPATH, home_btn)
    home_btn_element.click()

    tt.sleep(7)
profile='flo.w_ers'

def scroll():
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

def fp():
    follow_buttons = driver.find_elements(By.XPATH, "//div[text()='Follow']")
       
    for button in follow_buttons:
        button.click()
        tt.sleep(2)
        
def user_profile(username):
    profile_picture_alt = f"{username}'s profile picture"

    xpath_expression = f"//img[contains(@alt, \"{profile_picture_alt}\")]"
    image_element = driver.find_element(By.XPATH, xpath_expression)
    image_element.click()
    tt.sleep(10)
  

def follow(profile):


    try:
        search_btn = "//*[local-name()='svg' and @aria-label='Search' and @role='img']"
        search_btn_element = driver.find_element(By.XPATH, search_btn)
        search_btn_element.send_keys(profile)
        tt.sleep(7)
        search_btn_element.send_keys(Keys.ENTER)
        
        # print('i am okay 1')
    except:
        pass
    try:
        search_btn_element.click()
        input_xpath_expression = "//input[@aria-label='Search input' and @placeholder='Search']"
        search_input_element = driver.find_element(By.XPATH, input_xpath_expression)
        search_input_element.send_keys(profile)
        tt.sleep(6)
        search_input_element.send_keys(Keys.ENTER)
        
        tt.sleep(8)
        span_xpath_expression = f"//span[contains(text(), '{profile}')]"
        span_element = driver.find_element(By.XPATH, span_xpath_expression)
        
        span_element.click()
        tt.sleep(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.execute_script("window.scrollTop(0, document.body.scrollHeight);")
        tt.sleep(5)
        
        
    except:
        pass

    image_xp=f"//img[contains(translate(@alt, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{profile.lower()}')]"
    image_element = driver.find_elements(By.TAG_NAME,'img')
    aggw_div = driver.find_elements(By.XPATH, image_xp)
   
    image_info_list = []

    for image_element in image_element:
        src = image_element.get_attribute('src')
        alt = image_element.get_attribute('alt')
        
        if 'profile' in alt.lower():
            continue
       
        dateobj=extract_and_convert_date(alt)
        if dateobj is not None:
            image_info_list.append({
                'src': src,
                'alt': alt,
                'date': dateobj
            })

    most_recent_image = max(image_info_list, key=lambda x: x['date'])
   


    image_xp = f"//img[contains(@src, '{most_recent_image['src']}')]"

    # Find the img element with the most recent src
    most_recent_image_element = driver.find_element(By.XPATH, image_xp)

    # Click on the most recent image
    # most_recent_image_element.click()
    parent_container = most_recent_image_element.find_element(By.XPATH, './ancestor::div[@class="_aagu"]')

    # Click on the parent container
    parent_container.click()
    tt.sleep(7)
    liked_element = driver.find_element(By.XPATH, "//a[contains(@href, 'liked_by')]")
    liked_element.click()
    tt.sleep(7)
    class_name ="//div[@role='dialog']"
    el = driver.find_element(By.XPATH, class_name)
    y='/html/body/div[7]/div/div/div/div/div/div/div/div[2]'
    
    # counter=0
    # while counter<3:
    #     follow_buttons = driver.find_elements(By.XPATH, "//div[text()='Follow']")
    #     if len(follow_buttons)<1:
    #         scroll()
    #         counter+=1
    #         continue
    #     else:
    #         if counter>0:
    #             counter=0
    #         fp()
    close_pop="//*[local-name()='svg' and @aria-label='Close' and @role='img']"
    
    action=ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH, close_pop)).click().perform()
    tt.sleep(2)
    close_pop="//*[local-name()='svg' and @aria-label='Close' and @role='img']"
    # driver.find_element(By.XPATH, close_pop).click()
    action.move_to_element(driver.find_element(By.XPATH, close_pop)).click().perform()
   
    
        
    
    
   
    tt.sleep(15)
    


follow(profile)


def ufbtn():
    
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
    return(rv)
def unfollow(lim,username):
    home()
    tt.sleep(8)
    user_profile(username)
    fobtn="//a[contains(@href, 'following')]"
    driver.find_element(By.XPATH,fobtn).click()
    tt.sleep(5)
    follow_buttons = driver.find_elements(By.XPATH, "//div[text()='Following']")
    counter=0
    l=0
    while counter<3 and l<lim:
        if len(follow_buttons)<1:
            scroll()
            counter+=1
            continue
        else:
            if counter>0:
                counter=0
            li=ufbtn()
            l+=li
            
    close_pop="//*[local-name()='svg' and @aria-label='Close' and @role='img']"
    driver.find_element(By.XPATH, close_pop).click()   
    
    
   
    tt.sleep(30)
# unfollow(50,usern)
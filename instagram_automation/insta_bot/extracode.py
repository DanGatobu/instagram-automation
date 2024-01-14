n_scrolls =5
    # for i in range(1, n_scrolls):
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # tt.sleep(2)
        

    # follow_buttons = driver.find_elements(By.XPATH, "//div[text()='Follow']")

    # # # Click on each 'Follow' button

    # for button in follow_buttons:
    #     button.click()
    #     tt.sleep(3)  # 
    # # follow_button_text = "Follow"
    # counter=5
    # while counter>0:
        # driver.execute_script("window.scrollBy(0, 300);")
        # counter-=1
        # scroll_element = driver.find_element(By.XPATH, "//div[@role='dialog']")

    # Scroll using the mouse wheel
        # action = ActionChains(driver)
        # action.move_to_element(scroll_element).perform()
        # action.send_keys_to_element(scroll_element, Keys.ARROW_DOWN).perform()
        # pyautogui.scroll(-10)

        # tt.sleep(3)
            # driver.execute_script("arguments[0].scrollBy(0,arguments[0].scrollHeight)", scrollbar)
    # dig='/html/body/div[4]/div/div[2]/div/div'#'//*[@role="dialog"]'
    # focusdig = driver.find_element(By.XPATH, dig)
    # focusdig.click()
    # try:
    #     dialog_element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@class="x7r02ix xf1ldfh x131esax xdajt7p xxfnqb6 xb88tzc xw2csxc x1odjw0f x5fp0pe" and @role="dialog"]'))
    #     )
    #     dialog_element.click()
    #     print('clicked')
    # except Exception as e:
    #     print(f"Could not click on the element: {e}")

    # # If the above fails, try clicking on the parent div
    # try:
    #     parent_element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@class="x1ja2u2z x1afcbsf x1a2a7pz x6ikm8r x10wlt62 x71s49j x6s0dn4 x78zum5 xdt5ytf xl56j7k x1n2onr6" and @role="dialog"]'))
    #     )
    #     parent_element.click()
    # except Exception as e:
    #     print(f"Could not click on the parent element: {e}")
    # text_to_find = "Likes"

# Use XPath to find the h1 element with the specified text
    # try:
    #     h1_element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, f'//h1[contains(text(), "{text_to_find}") and @tabindex="-1"]'))
    #     )
    #     # Do something with the h1 element, e.g., print its text
    #     print(h1_element.text)
    #     h1_element.click()
    # except Exception as e:
    #     print(f"Could not find h1 element with text '{text_to_find}': {e}")
    # driver.execute_script("arguments[0].click();", focusdig)
    # actionChain = webdriver.ActionChains(driver)


    # scroll_script = "arguments[0].scrollTop = arguments[0].scrollHeight;"
    # count = 0

    # while(count < 100):
    # last_count = len(driver.find_elements(By.XPATH, "//div[text()='Follow']"))
    
    # scr(driver)
    
    # dialog_element = driver.find_element(By.XPATH, "//div[@role='dialog']")
    # dialog_element.click()
    # driver.execute_script("arguments[0].click();", dialog_element)
    # driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', dialog_element)
    # scrollbar = driver.find_element(By.CSS_SELECTOR, '[class*="Igw0E"][class*="IwRSH"][class*="eGOV_"][class*="vwCYk"][class*="i0EQd"]')
# Use JavaScript to scroll the element into view
    # driver.execute_script("arguments[0].scrollBy(0,350);", scrollbar)
    
    # Create an ActionChains object
    # actions = ActionChains(driver)
    # scroll_origin = ScrollOrigin.from_element(iframe)
    # ActionChains(driver)\
        # .scroll_from_origin(scroll_origin, 0, 200)\
        # .perform()

# Move the mouse to the center of the element
    # actions.move_to_element(el).perform()
    # actions.scroll_by_amount(0, 579).perform()
    # actions.send_keys(Keys.DOWN).perform()
   
        # f=driver.find_element(By.XPATH, "//div[text()='Follow']")
        # driver.execute_script("arguments[0].scrollIntoView();", f)
        # driver.execute_script(scroll_script, focusdig)
    # tt.sleep(4)  # Add a delay to allow time for the followers to load
    # new_count = len(driver.find_elements(By.XPATH, "//div[text()='Follow']"))
        
        # break  # Exit the loop 
        # class_name ="//div[@role='dialog']"
    # el = driver.find_element(By.XPATH, class_name)
    # for i in range(5):
    #     driver.execute_script("arguments[0].scrollTo(0,arguments[0].scrollHeight)", el)
    #     tt.sleep(3)
    
    
    # try:
        # follb=driver.find_elements(By.XPATH, "//button")
        # follb=driver.find_elements(By.XPATH,  "//div[text()='Following']")
        # print(follb.text)
        # follb.click()
        # for k,i in enumerate(follb):
        #     if k==0 or k==1:
        #         continue
            
        #     actions = ActionChains(driver)
            # unfollow_button = driver.find_element(By.XPATH, "//button[text()='Unfollow']")
            # unfollow_button.click()
            # tt.sleep(3)
            # scroll_delta_x = 0  # No horizontal scroll
            # scroll_delta_y = 500  # Scroll down by 200 pixels
            # actions.move_to_element(i).perform()
            # driver.execute_script("window.scrollTo(0, 400)")

           
            
            # i.click()
            # driver.execute_script("arguments[0].click();", i)
            # break
            # print(' niko hapa',i.text)
        
    # except Exception as e:
    #     print ('thissss',e)
    #     pass
    # try:
        # follb.click()
        # driver.execute_script("arguments[0].click();", follb)
    # except Exception as e:
    #     print (e)
    #     pass
    # unfb=follow_buttons = driver.find_element(By.XPATH, "//div[contains(@class, '_ap3a') and contains(@class, '_aaco') and contains(@class, '_aacw') and contains(@class, '_aad6') and contains(@class, '_aade') and contains(text(), 'Follow')]")
    # try:
    #     driver.execute_script("arguments[0].click();", unfb)
    # except Exception as e:
    #     print (e)
    #     pass
    # tt.sleep(2)
#     try:
#         # driver.find_element(By.XPATH, y).click()
#         #driver.execute_script("arguments[0].scrollTop = 300")
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         driver.execute_script("window.scrollTo(200, 300);")


#         scroll_element = driver.find_element(By.XPATH, "//div[@role='dialog']")
#         try:
#             driver.execute_script("window.scrollTo(0, 300)")
#         except:
#             pass
        
#         try:
#             driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',scroll_element)
#         except:
#             pass
        
        
              
       
#         try:
#             driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', scroll_element)
#         except:
#             pass
#         try:
#             driver.execute_script('''
#     var fDialog = document.querySelector('div[role="dialog"]);
#     fDialog.scrollTop = fDialog.scrollHeight
# ''')
#         except:
#             pass
        
#     except Exception as e:
#         print(e)
#         pass

    
    # try:
    #      driver.execute_script( 'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;') 
    # except:
    #     pass
    # try:
    #     # el.click()
    #     actions = ActionChains(driver)
    #     actions.send_keys(Keys.END).perform()
    # except:
    #     pass
    # try:
    #     # el.click()
        # vd=driver.find_element(By.XPATH, y)
        # driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',follb)
    # except:
        # pass
    # try:
    #     driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', el)
    # except:
    #     pass
    # try:
    #     # el.click()
    #     actions = ActionChains(driver)
    #     actions.move_to_element(el).send_keys(Keys.END).perform()
    # except:
    #     pass
    # tr="//div[@class='isgrP']"
    # try:
    #     er=driver.find_element(By.XPATH, tr)
    #     # er.click()
    #     driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', er)
    # except:
    #     pass
    # try:
    #     er=driver.find_element(By.XPATH, tr)
    #     # er.click()
    #     actions = ActionChains(driver)
    #     actions.move_to_element(er).send_keys(Keys.END).perform()
    # except:
    #     pass
    # image="//div[img]"
    # try:
    #     er=driver.find_element(By.XPATH, image)
    #     # er.click()
    #     driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', er)
    # except:
    #     pass
    # try:
    #     er=driver.find_element(By.XPATH, image)
    #     # er.click()
    #     actions = ActionChains(driver)
    #     actions.move_to_element(er).send_keys(Keys.END).perform()
    # except:
    #     pass
    
    
    

    
    

    # follow_buttons = driver.find_elements(By.XPATH, "//div[text()='Follow']")
    # for button in follow_buttons:
    #     button.click()
    #     tt.sleep(3)  # 
    
        
        
    
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import ElementClickInterceptedException

EMAIL = ""
PWD = ""
# add your details
SIMILAR_ACCOUNT = ""
# add your target account/user

class InstaFollower():

    def __init__(self): 
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options = options, service= Service(''))
        # add your chrmomedriver
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/") 
        sleep(2)
        email = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
        
        email.send_keys(EMAIL)
        password.send_keys(PWD)
        
        password.send_keys(Keys.ENTER)

    def find_follwers(self, target_user):
        sleep(10)
         # enter username of the target person
        enter_name = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_++"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[2]/div/div')
        enter_name.send_keys(target_user)
        sleep(3)
        # click on user that you searched
        self.driver.find_element(By.CSS_SELECTOR, '.fuqBx a').click()
        sleep(5)
        # click on followers, this will open followers pop up window
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section'
                                                       '/ul/li[2]/a/div')
        followers.click()
        sleep(5)
        # select the scrollable part of the popup window
        pop_up_window = self.driver.find_element(By.CLASS_NAME, 'isgrP')
        # scroll down to load more and more followers
        for i in range(4):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', pop_up_window)
            sleep(2)
    
    def follow(self):
        followers_list = self.driver.find_elements(By.CSS_SELECTOR, '.PZuss li button')
        for follower in followers_list:
            try:
                follower.click()
                sleep(2)
            except ElementClickInterceptedException:
                self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]').click()
                sleep(2)

mrbot = InstaFollower()
mrbot.login()
mrbot.find_follwers(SIMILAR_ACCOUNT)
mrbot.follow()

import time
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium import webdriver


class Webdriver_PJe(webdriver.Chrome):
    #def __init__(self):
        #super().__init__()
    frame_logar_ID = "ssoFrame"
    username_CSS_SELECTOR = "input#username"
    password_CSS_SELECTOR = "input#password"
    logar_ID = "kc-login"
    
    def logar(self, username,password):
        frame_logar = self.find_element(By.ID, self.frame_logar_ID)
        self.switch_to.frame(frame_logar)
        username_element = self.find_element(By.CSS_SELECTOR, self.username_CSS_SELECTOR)
        password_element = self.find_element(By.CSS_SELECTOR, self.password_CSS_SELECTOR)
        username_element.send_keys(username)
        time.sleep(0.5)
        password_element.send_keys(password)
        time.sleep(0.5)
        logar_element = self.find_element(By.ID, self.logar_ID).click()

        


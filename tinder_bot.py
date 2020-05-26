from selenium import webdriver
from time import sleep
from secrets import username, password
class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://tinder.com')
        print('opened tinder webpage')
        sleep(2)
        try:
            fb_btn=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]')
            fb_btn.click()
        except:
            # more_option_btn=self.driver.find_element_by_name('MORE OPTIONS')
            # print(more_option_btn, "befor xpath")
            more_option_btn=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
            more_option_btn.click()
            # fb_btn=self.driver.find_element_by_name('LOG IN WITH FACEBOOK')
            # print(fb_btn)
            fb_btn=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]')
            fb_btn.click()
            #  try:
            #     print('tyring for fb login before more options')
            #     fb_btn=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]')
            #     print(fb_btn)
            #     fb_btn.click()
            # except:
            #     print('after try now in expext')
            #     more_option_btn=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
            #     print(more_option_btn)
            #     more_option_btn.click()
            #     print('trying for fb login after more option')
            #     fb_btn=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]')
            #     fb_btn.click()
        print('waiting for popup to open')
        while(len(self.driver.window_handles)==1):
            sleep(1)
        print('fb login popup opened, switching to popup')
        #switch to pop window
        base_window=self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        print("entered email")
        password_in= self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)
        print("entered password")
        login_btn=self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        self.driver.switch_to.window(base_window)
        print('logged into tinder')
        sleep(20)
        try:
            allow_location_btn= self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            allow_location_btn.click()
            allow_location_btn= self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            allow_location_btn.click()
        except:
            allow_location_btn=0
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()
        print('right swiped')
    def dislike(self):
        dislike_btn=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()
        print('left swiped')
    def autoswipe(self):
        while True:
            sleep(3)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()
    
    def close_popup(self):
        popup  = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup.click()
        print('removed popup')
    def close_match(self):
        match_popup= self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()
        print('removed match popup')
bot= TinderBot()
bot.login()
sleep(2)
bot.autoswipe()
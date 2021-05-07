from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random

class Call():
    def __init__(self):
        self.driver = webdriver.Chrome('D:\drivers\chromedriver')
        self.driver.implicitly_wait(15)   #隐性等待
    
    def login(self):
        try:
            self.driver.get('http://10.170.36.104:8883/oms/jsp/login/index.jsp')
        finally:
            pass
            
        input = self.driver.find_element_by_id('ubean.userName')
        input.clear()
        input.send_keys('username')

        input = self.driver.find_element_by_id('ubean.passWord')
        input.clear()
        input.send_keys('password')

        login_bt = self.driver.find_element_by_id('btnLogin')
        login_bt.click()
            
    def click_qd_or_qt(self,tag):
        # iframe
        self.driver.switch_to.frame('frames')
        # driver.switch_to.frame('mainFrameSet')
        self.driver.switch_to.frame('right')

        iframe = self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[3]/td/iframe')
        self.driver.switch_to.frame(iframe)

        
        # 签到或签退WebElement
        element = self.driver.find_element_by_id(tag)
        element.click()
        
        time.sleep(3)
        # self.driver.switch_to.default_content()
        self.driver.switch_to.alert.accept()
        time.sleep(3)        # 一定要等几秒，javascript执行需要时间
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    # 随机等待秒数
    wait_time = random.randint(0,120)
    print(wait_time)
    time.sleep(wait_time)
    
    call = Call()
    call.login()
    call.click_qd_or_qt('qd')
    call.tearDown()
from selenium import webdriver
from  pyshadow.main  import  Shadow 
import time
import warnings
import os 
import shutil
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import random
from selenium.webdriver.common.by import By
import json
warnings.filterwarnings('ignore')

class CommonFunc: 
    def __init__(self) -> None:
        pass

    # 初始化webdriver
    def init_web_driver(self, chrome_data_dir):
        options=ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False) # 屏蔽webdriver特征
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument('--user-data-dir=' + chrome_data_dir)

        driver = webdriver.Chrome(options=options, executable_path='./chromedriver')
        return driver

    # 获取浏览器文件夹路径
    def get_chrome_data_dir(self, dir_name):
        try:
            curdir =os.path.dirname(__file__)+'\\'+dir_name
            os.mkdir(curdir)
            return curdir
        except Exception as e:
            print(e)
            return os.path.dirname(__file__)+'\\'+dir_name

    # 获取class元素text文本
    def get_text(self, driver, css_class,attemp_cnt = 10):
        cnt = 0
        while cnt < attemp_cnt:
            try:
                amount_ele = driver.find_element(By.CSS_SELECTOR,css_class)
                return amount_ele.text
            except:
                time.sleep(2)
                cnt += 1
        return -1
    # 获取class[index]元素text文本
    def get_text_from_list(self, driver, css_class,index,attemp_cnt = 10):
        cnt = 0
        while cnt < attemp_cnt:
            try:
                amount_ele = driver.find_elements(By.CSS_SELECTOR,css_class)
                return amount_ele[index].text
            except:
                time.sleep(2)
                cnt += 1
        return -1

    # 获取小狐狸钱包余额
    def get_amount(self, driver, attemp_cnt = 10):
        driver.switch_to.window(driver.window_handles[1])
        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#')

        return CommonFunc.get_text(self, driver, '.currency-display-component__text',attemp_cnt)

    # 获取class元素模拟按钮点击
    def press_button(self, driver, css_class,atemp_cnt = 10):
        cnt = 0
        while cnt < atemp_cnt:
            try:
                button = driver.find_element(By.CSS_SELECTOR,css_class)
                button.click()
                time.sleep(2)
                return True
            except:
                time.sleep(2)
                cnt += 1
        return False
    # 获取class[index]元素模拟按钮点击
    def press_button_from_list(self, driver, css_class,index,atemp_cnt = 10):
        cnt = 0
        while cnt < atemp_cnt:
            try:
                button = driver.find_elements(By.CSS_SELECTOR,css_class)
                button[index].click()
                time.sleep(2)
                return True
            except:
                time.sleep(2)
                cnt += 1
        return False
    # 获取class[index]元素再根据名称筛选模拟按钮点击
    def press_button_from_list_byName(self, driver, css_class,button_name,atemp_cnt = 10):
        cnt = 0
        while cnt < atemp_cnt:
            try:
                button_list = driver.find_elements(By.CSS_SELECTOR,css_class)
                for button in button_list:
                    if button.text == button_name:
                        button.click()
                        return True
                time.sleep(2)
                cnt += 1
            except:
                time.sleep(2)
                cnt += 1
        return False

    # 输入金额
    def send_keys(self, driver, css_class,key,atemp_cnt = 10):
        cnt = 0
        while cnt < atemp_cnt:
            try:
                input_amount = driver.find_element(By.CSS_SELECTOR,css_class)
                input_amount.clear()
                input_amount.send_keys(key)
                return True
            except:
                time.sleep(2)
                cnt += 1
        return False

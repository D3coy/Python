import vk_api
import requests
import selenium
import time
import os
import re
import random
from selenium.webdriver.chrome.options import Options as ChromeOpt
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime

class Config:
    token = None
    version = '5.131'

class app:
    def __init__(self):
        self.login = ''
        self.password = ''

    def __str(self, obj):
        if isinstance(obj, list or tuple):
            str_values = (str(val) for val in obj)
            return (',').join(str_values)
        return str(obj)

    def call(self, method, **params):
        """
        VK_API methods call function
        """
        
        __prefix = 'https://api.vk.com/method/'
        url = __prefix + method
        params = {k: self.__str(v) for k,v in params.items() if v != None}
        if Config.token:
            params['access_token'] = Config.token
        if Config.version:
            params['v'] = Config.version 
        
        request = requests.get(url, params=params)
        return request.json()

    def get_reposts(self, vk_token):
        """
        Получение репостов
        # access_token, из get_access_token(f)
        # , ID группы в вк
        # , postID, номер поста в группе
        """
        
        params = {
            'access_token': vk_token,
            'owner_id': "",
            'post_id': "",
            'count': 300
        }
        result = self.call('wall.getReposts', **params)
        return result.get('response').get('profiles')

    def generate_winners(self, rep):
        for i in range(3):
            time.sleep(1)
            random.seed(datetime.now().timestamp())
            num = random.randrange(len(rep))
            print('{} место | {} {} (id{})'.format(i+1, rep[num].get('first_name'), rep[num].get('last_name'), rep[num].get('id')))

    def app_main(self, token):
        vk_session = vk_api.VkApi(self.login, self.password)
        vk_session.auth()

        self.vk = vk_session.get_api()
        reposters = self.get_reposts(token)
        self.generate_winners(reposters)

class browser(app):
    def send_keys(self, element, arg):
        """
        [Internal]

        Clicks two times on the Selenium element.

        :param element: Selenium element
        :type element: Selenium object
        :param arg: Text or Keys to be sent to the element
        :type arg: str or selenium.webdriver.common.keys

        Usage:

        >>> #Defining the element:
        >>> element = lambda: self.driver.find_element_by_id("example_id")
        >>> #Calling the method with a string
        >>> self.send_keys(element(), "Text")
        >>> #Calling the method with a Key
        >>> self.send_keys(element(), Keys.ENTER)
        """
        try:
            if arg.isprintable():
                element.clear()
                element.send_keys(Keys.CONTROL, 'a')
            element.send_keys(arg)
        except Exception:
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.click()
            if arg.isprintable():
                actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE)
            actions.send_keys(Keys.HOME)
            actions.send_keys(arg)
            actions.perform()

    def login_vk(self):
        xpath_login = "//input[contains(@class, \"oauth\")][@name = \"email\"]"
        xpath_password = "//input[contains(@class, \"oauth\")][@name = \"pass\"]"
        xpath_entry = "//button[contains(@class, \"oauth_button\")]"
        login = lambda: self.driver.find_element(By.XPATH, xpath_login)
        password = lambda: self.driver.find_element(By.XPATH, xpath_password)
        button = lambda: self.driver.find_element(By.XPATH, xpath_entry)

        time.sleep(1)
        self.send_keys(login(), self.login)
        time.sleep(1)
        self.send_keys(password(), self.password)
        time.sleep(1)
        button().click()
        time.sleep(2)

    def get_access_token(self):
        options = ChromeOpt()
        options.binary_location = "C:\\Program Files (x86)\\Chromium\\chrome.exe"
        
        driver_path_travel = os.path.join(os.path.dirname(__file__)).split("\\")[1:-1]
        driver_path = os.path.join('E:', os.sep, *driver_path_travel, 'drivers_selenium', 'chromedriver.exe')

        self.driver = selenium.webdriver.Chrome(options=options, executable_path=driver_path)
        #self.driver.set_window_position(-1000, 0)
        auth_1 = "https://oauth.vk.com/authorize?"
        # Stealth improvements to the driver (works great)
        import selenium_stealth
        selenium_stealth.stealth(self.driver,
        languages=["ru-RU", "ru"],
        vendor="",
        platform="Win32",
        fix_hairline= True
        )
        self.driver.get(auth_1)
        self.login_vk()
        return re.search('(token=)(.*)(&expires_in)', self.driver.current_url).group(2)

hBrowser = browser()
token = hBrowser.get_access_token()

hApp = app()
hApp.app_main(token)
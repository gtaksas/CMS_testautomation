'''Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import mouse
import time
import unittest
import HtmlTestRunner

driver=webdriver.Chrome()#(executable_path="C:\\Python\\chrome_driver\\chromedriver.exe")

class VgCms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #cls.driver=webdriver.Chrome(executable_path="C:\\Python\\chrome_driver\\chromedriver.exe")
        cls.driver=driver

        #LOGIN

        cls.driver.get("http://CMS_PATH_HERE/")
        cls.driver.implicitly_wait(5)
        
        cls.user = cls.driver.find_element_by_xpath("//input[1]")
        cls.password = cls.driver.find_element_by_xpath("//input[@type='password']")
        cls.submit = cls.driver.find_element_by_xpath("//button[1]")

        cls.user.send_keys("YOUR_EMAIL_ADRESS_HERE")
        cls.password.send_keys("YOUR_PASSWORD_HERE")
        cls.submit.click()

        #LOGIN END

        cls.driver.implicitly_wait(5)

        #selectVG

        #self.driver.get("http://CMS_PATH_HERE/domain-select")
        
        cls.vg = cls.driver.find_element_by_xpath("//p[text()='Világgazdaság']")

        cls.vg.click()
        
        #selectVG END


    def test_openArticles_pageEditor(self):
        
        #openArticles_pageEditor

        self.driver.get("http://CMS_PATH_HERE/admin/articles/page-editor/bd78bfa0-a0ae-4ff2-82ec-e23d0c0a17a8?type=article&prevUrl=%2Fadmin%2Farticles&&&&&fields%5B%5D=title&fields%5B%5D=publicState&fields%5B%5D=printStatus&fields%5B%5D=isActive&fields%5B%5D=isPrint&fields%5B%5D=author&fields%5B%5D=isPrintShow&fields%5B%5D=publishDate&fields%5B%5D=isActiveShow")

        #openArticles_pageEditor END


    def test_openStatistics(self):
        
        #openStatistics

        self.driver.get("http://CMS_PATH_HERE/admin/users-statistics")

        #openStatistics END


    def test_scrolldownInputField(self):

        #scrolldownInputField

        self.driver.get("http://CMS_PATH_HERE/admin/users-statistics")
        
        self.inputField = self.driver.find_element_by_xpath ("//app-select-form-control-old[1]") #("//input[2]")

        self.inputField.click()
        
        #scrolldownInputField END'''

    def test_findScrolldownListElements(self):

        self.driver.get("CMS_PATH_HERE/admin/users-statistics")

        self.inputField = self.driver.find_element_by_xpath("//app-select-form-control-old[1]") #("//input[2]")

        self.inputField.click()

        self.listElement = self.driver.find_element_by_xpath("//nz-option-item[1]")

        self.listElement.click()

        time.sleep(5)



if __name__ == '__main__':
    
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='YOUR_PATH_FOR_SAVING_TEST_RESULT_FILES'))


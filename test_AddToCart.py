import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_google_search_page(self):
        driver = self.driver
        driver.get("https://www.flipkart.com/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.XPATH,"//span[text()='✕']").click()
        driver.find_element(By.XPATH,"//input[@title='Search for Products, Brands and More']").send_keys("Macbook air m2")
        driver.find_element(By.XPATH,"//button[@title='Search for Products, Brands and More']").click()
        driver.find_element(By.XPATH,"//a[@class='_1fQZEK']").click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1]) 
        driver.find_element(By.XPATH,"//button[text()='Add to cart']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//span[text()='Cart']/parent::a").click()
        time.sleep(3)
        ActualproductName=driver.find_element(By.XPATH,"//a[@class='_2Kn22P gBNbID']").text
        ExpectedProductName="APPLE 2022 MacBook AIR M2 - (8 GB/256 GB SSD/Mac OS Monterey) MLY33HN/A"
        assert ActualproductName==ExpectedProductName

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()